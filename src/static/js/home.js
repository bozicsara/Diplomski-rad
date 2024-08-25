import { create_call } from "./video.js";

const loader = document.querySelector(".loader");
const icon = document.querySelector(".fa-video");

const socket = io.connect("http://localhost:5000");
socket.on("pair", function (msg) {
  console.log("Pairing...");
  loader.hidden = true;
  icon.style.display = "";
  create_call();
});

getAllEntities();

callOperation();

function callOperation() {
  document.getElementById("chatButton").addEventListener("click", function () {
    console.log("Chat button clicked!");
    icon.style.display = "none";
    loader.hidden = false;
    socket.emit("incoming_call", { data: "I want to speak to the pharmacist." });
  });
}

async function getAllEntities() {
  try {
    const response = await fetch(`/lek/all`, { method: "get" });
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();
    if (data.Status === "Error") throw new Error(data.Message);

    const formatedData = formatData(data.Data);
    createHomeLayout();
    populateHomeLayout(formatedData);
  } catch (error) {
    console.error("There was a problem fetching the data:", error.message);
  }
}

async function getSearchedEntities(searchParam) {
  try {
    const response = await fetch(
      `/lek?${new URLSearchParams({ search_param: searchParam })}`,
      { method: "get" }
    );
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();
    if (data.Status === "Error") throw new Error(data.Message);

    const formatedData = formatData(data.Data);
    populateHomeLayout(formatedData);
  } catch (error) {
    console.error("There was a problem fetching the data:", error.message);
  }
}

function formatData(data) {
  const formatedData = [];
  const dataSchema = {
    zapakovan_lek_id: "",
    doziranje: "",
    naziv: "",
    nezeljenaDejstva: "",
    opis: "",
    cena: "",
    jacina: "",
    zaliha: "",
    slikaUrl: "",
  };
  for (let item of data) {
    const newItem = Object.create(dataSchema);
    newItem.doziranje = item.doziranje;
    newItem.naziv = item.naziv;
    newItem.nezeljenaDejstva = item.nezeljena_dejstva;
    newItem.opis = item.opis_namena;
    for (let zapakovani_lek of item.zapakovani_lekovi) {
      newItem.zapakovan_lek_id = item.id;
      newItem.cena = zapakovani_lek.cena + " RSD";
      newItem.jacina =
        zapakovani_lek.jacina + " " + zapakovani_lek.merna_jedinica_.naziv;
      newItem.zaliha = zapakovani_lek.zaliha;
      newItem.slikaUrl = zapakovani_lek.url;
      formatedData.push(JSON.parse(JSON.stringify(newItem)));
    }
  }
  return formatedData;
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

function createInputElement(maxValue) {
  const productQuantity = document.createElement("div");
  productQuantity.className = "product-quantity";

  const input = document.createElement("input");
  input.type = "text";
  input.id = "quantity";
  input.name = "quantity";
  input.value = "1";
  input.step = "1";
  input.min = "1";
  input.max = maxValue;
  input.style.color = "#8bf7d3";
  input.style.fontWeight = "bold";

  const quantityControls = document.createElement("div");
  quantityControls.className = "quantity-controls";

  const incrementButton = document.createElement("button");
  incrementButton.type = "button";
  incrementButton.addEventListener("click", function () {
    increment(input);
  });
  incrementButton.innerHTML = "▲";

  const decrementButton = document.createElement("button");
  decrementButton.type = "button";
  decrementButton.addEventListener("click", function () {
    decrement(input);
  });
  decrementButton.innerHTML = "▼";

  quantityControls.appendChild(incrementButton);
  quantityControls.appendChild(decrementButton);

  productQuantity.appendChild(input);
  productQuantity.appendChild(quantityControls);

  return { productQuantity, input };
}

function createCardElement(data) {
  const cardParent = document.createElement("div");
  cardParent.className = "col-md-6 pt-3 pb-3";

  const card = document.createElement("div");
  card.className = "card shadow-lg";
  card.style.borderRadius = "10px";
  card.style.height = "100%";

  const name = data.naziv + " " + data.jacina;

  const imageContainer = document.createElement("div");
  imageContainer.className = "d-flex justify-content-center";
  imageContainer.style.cursor = "pointer";
  imageContainer.style.height = "500px";
  imageContainer.style.paddingTop = "20px";

  const img = document.createElement("img");
  img.className = "card-img-top";
  img.src = data.slikaUrl;
  img.alt = "Image of " + name;
  img.style.height = "auto";
  img.style.objectFit = "contain";
  img.setAttribute("data-toggle", "modal");
  img.setAttribute("data-target", "#modalElement");
  img.addEventListener("click", () => {
    putDataInModal(data);
  });

  imageContainer.appendChild(img);
  card.appendChild(imageContainer);

  const cardBody = document.createElement("div");
  cardBody.className = "card-body";

  const cardTitle = document.createElement("h5");
  cardTitle.className = "card-title text-center";
  cardTitle.innerHTML = name;

  const cardSubTitle = document.createElement("h5");
  cardSubTitle.className = "card-title text-center mb-3";
  cardSubTitle.innerHTML = data.cena;

  const footerSection = document.createElement("div");
  footerSection.className = "d-flex justify-content-center";
  footerSection.style.gap = "10px";
  footerSection.style.overflowX = "auto";

  const { productQuantity, input } = createInputElement(data.zaliha.toString());

  const addToCart = document.createElement("button");
  addToCart.addEventListener("click", function () {
    addInCartAction(parseInt(input.value), data);
  });
  addToCart.type = "button";
  addToCart.className = "btn btn-primary button_moja_apoteka_bigger ";
  addToCart.style.width = "50%";
  addToCart.innerHTML = "Dodaj u korpu";

  footerSection.appendChild(productQuantity);
  footerSection.appendChild(addToCart);

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardSubTitle);
  cardBody.appendChild(footerSection);

  card.appendChild(cardBody);
  cardParent.appendChild(card);
  return cardParent;
}

function createHomeLayout(data) {
  const searchSection = document.createElement("div");
  searchSection.className = "d-flex justify-content-center pt-5 input-group";
  searchSection.style.width = "100%";
  searchSection.style.marginBottom = "40px";

  const searchInput = document.createElement("input");
  searchInput.id = "searchInput";
  searchInput.className = "form-control";
  searchInput.placeholder = "Pretraži...";
  searchInput.type = "text";
  searchInput.style.borderRadius = "18px";
  searchInput.style.border = "1px solid #ced4da";
  searchInput.style.width = "50%";
  searchInput.style.flex = "unset";
  searchInput.style.height = "42px";
  searchInput.addEventListener("input", debounce(handleSearch, 500));

  searchSection.appendChild(searchInput);

  const container = document.createElement("div");
  container.id = "container";
  container.className = "container";

  const root = document.getElementById("root");

  root.appendChild(searchSection);
  root.appendChild(container);
  root.appendChild(createModal());
}

function populateHomeLayout(data) {
  const container = document.getElementById("container");
  container.innerHTML = "";

  for (let i = 0; i < data.length; i++) {
    const row = document.createElement("div");
    row.className = "row justify-content-center g-5";
    for (let j = 0; j < 2; j++) {
      if (i + j < data.length) {
        console.log(data[i + j]);
        const card = createCardElement(data[i + j]);
        row.appendChild(card);
      }
    }
    container.appendChild(row);
    i++;
  }
}

function createModal() {
  const modal = document.createElement("div");
  modal.className = "modal fade";
  modal.id = "modalElement";
  modal.tabIndex = "-1";
  modal.role = "dialog";
  modal.setAttribute("aria-labelledby", "modalElementTitle");
  modal.setAttribute("aria-hidden", "true");

  const modalDialog = document.createElement("div");
  modalDialog.className = "modal-dialog modal-dialog-centered";
  modalDialog.style.minWidth = "70%";
  modalDialog.role = "document";

  const modalContent = document.createElement("div");
  modalContent.className = "modal-content";
  modalContent.style.width = "auto";

  const modalHeader = document.createElement("div");
  modalHeader.className = "modal-header";

  const modalTitle = document.createElement("h5");
  modalTitle.className = "modal-title";
  modalTitle.id = "modalElementTitle";
  modalTitle.innerHTML = "Title";

  const modalCloseButton = document.createElement("div");
  modalCloseButton.style.cursor = "pointer";
  modalCloseButton.className = "close";
  modalCloseButton.setAttribute("data-dismiss", "modal");
  modalCloseButton.setAttribute("aria-label", "Close");

  const modalCloseButtonSpan = document.createElement("span");
  modalCloseButtonSpan.setAttribute("aria-hidden", "true");
  modalCloseButtonSpan.innerHTML = '<i class="fa-solid fa-xmark"></i>';
  modalCloseButton.appendChild(modalCloseButtonSpan);

  modalHeader.appendChild(modalTitle);
  modalHeader.appendChild(modalCloseButton);

  const modalBody = document.createElement("div");
  modalBody.id = "modalElementBody";
  modalBody.className = "modal-body";

  const mainSection = document.createElement("div");
  mainSection.id = "mainModalSection";
  mainSection.className = "d-flex justify-content-around";

  modalBody.appendChild(mainSection);

  modalContent.appendChild(modalHeader);
  modalContent.appendChild(modalBody);

  modalDialog.appendChild(modalContent);

  modal.appendChild(modalDialog);

  return modal;
}

function putDataInModal(data) {
  const name = data.naziv + " " + data.jacina;

  const modalTitle = document.getElementById("modalElementTitle");
  modalTitle.innerHTML = name;

  const mainModalSection = document.getElementById("mainModalSection");
  mainModalSection.innerHTML = "";

  const imageContainer = document.createElement("div");
  imageContainer.className = "d-flex justify-content-center";
  imageContainer.style.maxWidth = "500px";
  imageContainer.style.maxHeight = "450px";

  const img = document.createElement("img");
  img.className = "m-3";
  img.src = data.slikaUrl;
  img.alt = "Image of " + name;
  img.style.maxWidth = "500px";
  img.style.objectFit = "contain";

  imageContainer.appendChild(img);

  const rightSection = document.createElement("div");
  rightSection.className = "m-3";
  rightSection.style.maxHeight = "500px";
  rightSection.style.overflowY = "auto";

  const rightDownSection = document.createElement("div");
  rightDownSection.className = "d-flex justify-content-center";
  rightDownSection.style.gap = "25px";

  const descriptionSection = document.createElement("div");

  const descriptionTitle = document.createElement("h5");
  descriptionTitle.innerText = "Opis";

  const description = document.createElement("p");
  description.innerText = data.opis;

  descriptionSection.appendChild(descriptionTitle);
  descriptionSection.appendChild(description);

  const doziranjeSection = document.createElement("div");

  const doziranjeTitle = document.createElement("h5");
  doziranjeTitle.innerText = "Doziranje";

  const doziranje = document.createElement("p");
  doziranje.innerText = data.doziranje;

  doziranjeSection.appendChild(doziranjeTitle);
  doziranjeSection.appendChild(doziranje);

  const nezeljenaDejstvaSection = document.createElement("div");

  const nezeljenaDejstvaTitle = document.createElement("h5");
  nezeljenaDejstvaTitle.innerText = "Neželjena dejstva";

  const nezeljenaDejstva = document.createElement("p");
  nezeljenaDejstva.innerText = data.nezeljenaDejstva;

  nezeljenaDejstvaSection.appendChild(nezeljenaDejstvaTitle);
  nezeljenaDejstvaSection.appendChild(nezeljenaDejstva);

  const { productQuantity, input } = createInputElement(data.zaliha.toString());

  const addToCartBtn = document.createElement("button");
  addToCartBtn.addEventListener("click", function () {
    addInCartAction(parseInt(input.value), data);
  });
  addToCartBtn.type = "button";
  addToCartBtn.className = "btn btn-primary button_moja_apoteka_smaller";
  addToCartBtn.style.width = "50%";
  addToCartBtn.innerHTML = "Dodaj u korpu";

  rightDownSection.appendChild(productQuantity);
  rightDownSection.appendChild(addToCartBtn);

  rightSection.appendChild(descriptionSection);
  rightSection.appendChild(doziranjeSection);
  rightSection.appendChild(nezeljenaDejstvaSection);
  rightSection.appendChild(rightDownSection);

  mainModalSection.appendChild(imageContainer);
  mainModalSection.appendChild(rightSection);
}

function addInCartAction(numberOfItem, item) {
  const cartIcon = document.getElementById("cart_icon");
  cartIcon.className = "fa-solid fa-cart-shopping fa-fade fa-2xl";

  workWithLocalStorage(numberOfItem, item);
}

function workWithLocalStorage(numberOfNewItem, newItem) {
  const key = newItem.naziv + " " + newItem.jacina;
  const value = { item: newItem, num: numberOfNewItem };
  if (localStorage.getItem(key) == null) {
    localStorage.setItem(key, JSON.stringify(value));
  } else {
    const oldValue = JSON.parse(localStorage.getItem(key));
    oldValue.num += numberOfNewItem;
    localStorage.setItem(key, JSON.stringify(oldValue));
  }
}

function debounce(func, delay) {
  let debounceTimer;
  return function () {
    const context = this;
    const args = arguments;
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => func.apply(context, args), delay);
  };
}

function handleSearch() {
  const searchTerm = document.getElementById("searchInput").value;
  getSearchedEntities(searchTerm);
}
