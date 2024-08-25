createContent(localStorage);

function crateheadline(content) {
  const headline = document.createElement("h4");
  headline.textContent = content;
  headline.className = "text-left";
  headline.style.paddingLeft = "10%";
  headline.style.fontWeight = "bold";
  headline.style.paddingTop = "30px";
  headline.style.paddingBottom = "30px";

  return headline;
}

function createSubmitButton() {
  const buttonContainer = document.createElement("div");
  buttonContainer.className = "d-flex justify-content-end";
  buttonContainer.style.paddingRight = "10%";

  const goToPaymentPageBtn = document.createElement("button");
  goToPaymentPageBtn.textContent = "Potvrdi";
  goToPaymentPageBtn.classList.add("btn");
  goToPaymentPageBtn.classList.add("btn-primary");
  goToPaymentPageBtn.classList.add("btn-lg");
  goToPaymentPageBtn.classList.add("button_moja_apoteka");

  goToPaymentPageBtn.addEventListener("click", () => {
    window.location.href = "/order";
  });

  buttonContainer.appendChild(goToPaymentPageBtn);

  return buttonContainer;
}

function createEmptyCart() {
  const image = document.createElement("img");
  image.setAttribute(
    "src",
    "https://cdn-icons-png.flaticon.com/512/2037/2037457.png"
  );
  image.style.width = "35%";

  return image;
}

function convertDataInUsableForm(data) {
  const filteredData = [];
  const objectForm = {
    id: 0,
    name: "",
    price: "",
    quantity: 0,
  };

  for (let i = 0; i < data.length; i++) {
    let value = JSON.parse(data.getItem(data.key(i)));
    let newObject = JSON.parse(JSON.stringify(objectForm));
    newObject.id = i;
    newObject.name = data.key(i);
    newObject.price = value.item.cena;
    newObject.quantity = value.num;
    filteredData.push(newObject);
  }

  return filteredData;
}

function createContent(data) {
  const contentContainer = document.createElement("div");
  contentContainer.className = "d-flex justify-content-center";

  let content =
    data.length == 0
      ? createEmptyCart()
      : createTable(convertDataInUsableForm(data));

  contentContainer.appendChild(content);
  const rootElement = document.getElementById("root");

  let headlineContent;
  headlineContent = data.length == 0 ? "" : "VAŠA KORPA";

  rootElement.appendChild(crateheadline(headlineContent));
  rootElement.appendChild(contentContainer);
  data.length != 0 && rootElement.appendChild(createSubmitButton());
}

function increment(quantityInput) {
  const currentValue = parseInt(quantityInput.value, 10);
  if (currentValue < 100) {
    quantityInput.value = currentValue + 1;
  }
}

function decrement(quantityInput) {
  const currentValue = parseInt(quantityInput.value, 10);
  if (currentValue > 1) {
    quantityInput.value = currentValue - 1;
  }
}

function createInputElement(value, id) {
  const productQuantity = document.createElement("div");
  productQuantity.className = "product-quantity";

  const input = document.createElement("input");
  input.type = "text";
  input.id = id;
  input.name = "quantity";
  input.value = value;
  input.step = "1";
  input.min = "0";
  input.max = "100";
  input.style.color = "#8bf7d3";
  input.style.fontWeight = "bold";

  const quantityControls = document.createElement("div");
  quantityControls.className = "quantity-controls";

  const incrementButton = document.createElement("button");
  incrementButton.type = "button";
  incrementButton.innerHTML = "▲";

  const decrementButton = document.createElement("button");
  decrementButton.type = "button";
  decrementButton.innerHTML = "▼";

  quantityControls.appendChild(incrementButton);
  quantityControls.appendChild(decrementButton);

  productQuantity.appendChild(input);
  productQuantity.appendChild(quantityControls);

  return { productQuantity, input, incrementButton, decrementButton };
}

function createTable(data) {
  const table = document.createElement("table");
  table.classList.add("table");
  table.classList.add("text-center");
  table.classList.add("table-bordered");
  table.style.width = "80%";
  table.style.backgroundColor = "#FDFDFD";
  table.style.border = "3px solid black";
  table.style.borderRadius = "10px";

  const thead = document.createElement("thead");

  const tr = document.createElement("tr");

  const thNaziv = document.createElement("th");
  thNaziv.setAttribute("scope", "col");
  thNaziv.textContent = "Naziv";
  tr.appendChild(thNaziv);

  const thCena = document.createElement("th");
  thCena.setAttribute("scope", "col");
  thCena.textContent = "Cena";
  tr.appendChild(thCena);

  const thKolicina = document.createElement("th");
  thKolicina.setAttribute("scope", "col");
  thKolicina.textContent = "Količina";
  tr.appendChild(thKolicina);

  const thObrisi = document.createElement("th");
  thObrisi.setAttribute("scope", "col");
  thObrisi.textContent = "Obriši";
  tr.appendChild(thObrisi);

  const thUkupno = document.createElement("th");
  thUkupno.setAttribute("scope", "col");
  thUkupno.textContent = "Ukupno";
  tr.appendChild(thUkupno);

  thead.appendChild(tr);

  const tbody = document.createElement("tbody");

  let totalPrice = 240.0;

  for (let item of data) {
    const tr = document.createElement("tr");

    const tdNaziv = document.createElement("td");
    tdNaziv.textContent = item.name;
    tr.appendChild(tdNaziv);

    const tdCena = document.createElement("td");
    tdCena.textContent = item.price;
    tr.appendChild(tdCena);

    const tdKolicina = document.createElement("td");
    tdKolicina.style.display = "flex";
    tdKolicina.style.borderStyle = "none";
    tdKolicina.style.justifyContent = "center";
    const { productQuantity, input, incrementButton, decrementButton } =
      createInputElement(item.quantity, item.id);
    input.addEventListener("change", () => {
      const itemQuantity = parseInt(input.value, 10);
      const quantity = updateItemInLocalStorage(item.name, itemQuantity);

      totalPrice -= total;
      total = price * itemQuantity;
      totalPrice += total;
      tdZbir.textContent = total + " RSD";

      if (quantity === 0) {
        const parentRow = productQuantity.parentElement.parentElement;
        const bodyElement = parentRow.parentElement;
        deleteRowInTable(
          bodyElement,
          parentRow,
          totalPrice,
          total,
          tdUkupno,
          item
        );
      } else {
        tdUkupno.textContent = "Ukupan iznos: " + totalPrice + " RSD";
      }
    });
    incrementButton.addEventListener("click", () => {
      const itemQuantity = parseInt(input.value, 10) + 1;
      input.value = itemQuantity;

      const quantity = updateItemInLocalStorage(item.name, itemQuantity);

      totalPrice -= total;
      total = price * itemQuantity;
      totalPrice += total;
      tdZbir.textContent = total + " RSD";

      if (quantity === 0) {
        const parentRow = productQuantity.parentElement.parentElement;
        const bodyElement = parentRow.parentElement;
        deleteRowInTable(
          bodyElement,
          parentRow,
          totalPrice,
          total,
          tdUkupno,
          item
        );
      } else {
        tdUkupno.textContent = "Ukupan iznos: " + totalPrice + " RSD";
      }
    });
    decrementButton.addEventListener("click", () => {
      const itemQuantity = parseInt(input.value, 10) - 1;
      input.value = itemQuantity;

      const quantity = updateItemInLocalStorage(item.name, itemQuantity);

      totalPrice -= total;
      total = price * itemQuantity;
      totalPrice += total;
      tdZbir.textContent = total + " RSD";

      if (quantity === 0) {
        const parentRow = productQuantity.parentElement.parentElement;
        const bodyElement = parentRow.parentElement;
        deleteRowInTable(
          bodyElement,
          parentRow,
          totalPrice,
          total,
          tdUkupno,
          item
        );
      } else {
        tdUkupno.textContent = "Ukupan iznos: " + totalPrice + " RSD";
      }
    });
    tdKolicina.appendChild(productQuantity);
    tr.appendChild(tdKolicina);

    const tdObrisi = document.createElement("td");
    const buttonObrisi = document.createElement("button");
    buttonObrisi.setAttribute("data-id", item.id);
    buttonObrisi.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    buttonObrisi.style.borderRadius = "15%";
    buttonObrisi.style.width = "30px";
    buttonObrisi.style.height = "30px";
    buttonObrisi.addEventListener("click", () => {
      const parentRow = buttonObrisi.parentElement.parentElement;
      const bodyElement = parentRow.parentElement;

      totalPrice = deleteRowInTable(
        bodyElement,
        parentRow,
        totalPrice,
        total,
        tdUkupno,
        item
      );
    });
    tdObrisi.appendChild(buttonObrisi);
    tr.appendChild(tdObrisi);

    const tdZbir = document.createElement("td");
    const price = parseFloat(item.price.match(/[\d\.]+/)[0]);
    let total = price * item.quantity;
    totalPrice += total;
    tdZbir.textContent = total + " RSD";
    tr.appendChild(tdZbir);

    tbody.appendChild(tr);
  }

  const tfoot = document.createElement("tfoot");

  const trDostava = document.createElement("tr");
  trDostava.style.borderWidth = "0px";
  trDostava.style.textAlign = "right";
  trDostava.style.marginTop = "100px";
  const tdDostava = document.createElement("td");
  tdDostava.setAttribute("colspan", "5");
  tdDostava.textContent = "Dostava: 240.00 RSD";
  trDostava.appendChild(tdDostava);
  tfoot.appendChild(trDostava);

  const trUkupno = document.createElement("tr");
  trUkupno.style.borderWidth = "0px";
  trUkupno.style.fontWeight = "bold";
  trUkupno.style.textAlign = "right";
  const tdUkupno = document.createElement("td");
  tdUkupno.style.fontWeight = "700";
  tdUkupno.style.color = "black";
  tdUkupno.setAttribute("colspan", "5");

  tdUkupno.textContent = "Ukupan iznos: " + totalPrice + " RSD";
  trUkupno.appendChild(tdUkupno);
  tfoot.appendChild(trUkupno);

  table.appendChild(thead);
  table.appendChild(tbody);
  table.appendChild(tfoot);

  return table;
}

function deleteRowInTable(
  tableBodyElement,
  tableRowElement,
  totalPrice,
  total,
  tdUkupno,
  item
) {
  tableBodyElement.removeChild(tableRowElement);

  deleteItemFromLocalStorage(item.name);

  totalPrice -= total;
  tdUkupno.textContent = "Ukupan iznos: " + totalPrice + " RSD";

  isTableEmpty(tableBodyElement);

  return totalPrice;
}

function isTableEmpty(tableBodyElement) {
  if (tableBodyElement.children.length == 0) {
    const rootElement = document.getElementById("root");
    rootElement.children[0].textContent = "";
    rootElement.removeChild(rootElement.lastChild);
    rootElement.lastChild.removeChild(rootElement.lastChild.firstChild);
    rootElement.lastChild.appendChild(createEmptyCart());
  }
}

function deleteItemFromLocalStorage(key) {
  localStorage.removeItem(key);
}

function updateItemInLocalStorage(key, value) {
  let item = JSON.parse(localStorage.getItem(key));
  if (value === 0) {
    localStorage.removeItem(key);
    return value;
  }
  item.num = value;
  localStorage.setItem(key, JSON.stringify(item));
  return value;
}
