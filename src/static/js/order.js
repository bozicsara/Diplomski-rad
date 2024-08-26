work();

const baseURL = "http://127.0.0.1:5000";

const Status = {
  SUCCESS: "Success",
  ERROR: "Error",
};

async function collectAllDataAndCreateEntities() {
  const firstNameInput = document.getElementById("firstName");
  const lastNameInput = document.getElementById("lastName");
  const emailInput = document.getElementById("email");
  const phoneInput = document.getElementById("phone");
  const addressInput = document.getElementById("address");

  if (
    !(
      firstNameInput.value &&
      lastNameInput.value &&
      emailInput.value &&
      phoneInput.value &&
      addressInput.value
    ) ||
    !localStorage.length
  )
    return createNotification(
      "Morate popuniti sva obavezna polja!",
      true
    );
  const userResponse = await createEntity(
    {
      ime: firstNameInput.value,
      prezime: lastNameInput.value,
      email: emailInput.value,
      broj_telefona: phoneInput.value,
    },
    "/korisnik"
  );
  console.log(userResponse);
  if (userResponse.Status === Status.ERROR)
    return createNotification("Greška prilikom kreiranja korisnika!", true);
  const orderResponse = await createEntity(
    {
      korisnik_id: userResponse.Data.id,
      adresa: addressInput.value,
      datum_vreme: new Date().getTime() / 1000,
    },
    "/narudzbina"
  );
  if (orderResponse.Status === Status.ERROR)
    createNotification("Greška prilikom kreiranja narudžbine!", true);
  console.log(orderResponse);
  return orderResponse.Data.id;
}

async function handleDataFromLocalStorageAndCreateEntites(orderID) {
  for (let i = 0; i < localStorage.length; i++) {
    const orderItem = JSON.parse(localStorage.getItem(localStorage.key(i)));
    const orderItemResponse = await createEntity(
      {
        narudzbina_id: orderID,
        zapakovan_lek_id: orderItem.item.zapakovan_lek_id,
        kolicina: orderItem.num,
      },
      "/stavka_narudzbine"
    );
    if (orderItemResponse.Status === Status.ERROR) {
      createNotification("Greška prilikom kreiranja stavke narudžbine!", true);
      return;
    } else {
      console.log(orderItemResponse);
    }
  }
  localStorage.clear();
  createNotification("Uspešna proudžbina!", false);
}

function work() {
  const finishShoppingBtn = document.getElementById("finishShoppingBtn");
  finishShoppingBtn.addEventListener("click", async function () {
    const orderID = await collectAllDataAndCreateEntities();
    if (!orderID) return;
    await handleDataFromLocalStorageAndCreateEntites(orderID);
  });
}

async function createEntity(data, url) {
  const response = await fetch(baseURL + url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

function createNotification(msg, fail) {
  const alert = document.createElement("div");
  alert.id = fail ? "infoAlertFail" : "infoAlertSuccess";
  alert.classList.add("alert");
  alert.classList.add(fail ? "alert-danger" : "alert-success");
  alert.classList.add("fade");
  alert.classList.add("show");
  alert.setAttribute("role", "alert");
  alert.innerHTML = msg;
  alert.style.fontWeight = "400";
  alert.style.fontSize = "1.2rem";

  if (!fail) {
    const inputs = document.querySelectorAll("input");
    inputs.forEach((input) => {
      input.value = "";
    });
  }

  document.body.appendChild(alert);
  setTimeout(
    () => {
      alert.remove();
    },
    fail ? 3000 : 5000
  );
}
