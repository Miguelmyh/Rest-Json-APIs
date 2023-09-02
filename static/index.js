const btns = document.querySelectorAll(".delete-cupcake");
const form = document.querySelector("form");

for (btn of btns) {
  btn.addEventListener("click", deleteCupcake);
}

async function deleteCupcake() {
  console.log("hello");
  const id = this.getAttribute("data-id");
  await axios.delete(`/api/cupcakes/${id}`);
  this.parentElement.remove();
}

async function submitCupcake(e) {
  e.preventDefault();
  const flavor = form.querySelector('input[name="flavor"]').value;
  const size = form.querySelector('input[name="size"]').value;
  const rating = form.querySelector('input[name="rating"]').value;
  let img = form.querySelector('input[name="image"]').value;

  const cupcakeResp = await axios.post("/api/cupcakes", {
    flavor,
    size,
    rating,
    img,
  });

  cupcake = cupcakeResp.data.cupcake;
  let ul = document.querySelector("ul");
  let newInput = document.createElement("li");
  newInput.innerHTML = `${cupcake.flavor} - `;
  let newBtn = document.createElement("button");
  newBtn.classList.add("delete-cupcake");
  newBtn.setAttribute("data-id", cupcake.id);
  newBtn.innerHTML = "X";
  newInput.appendChild(newBtn);
  ul.appendChild(newInput);

  newBtn.addEventListener("click", deleteCupcake);
}

form.addEventListener("submit", submitCupcake);
