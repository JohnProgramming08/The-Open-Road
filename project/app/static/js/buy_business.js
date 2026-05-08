// Fetch data from HTML file
const bought = window.bought;

// Fetch all the necessary DOM elements
const buyButton = document.getElementById("buy-div");
const cancelButton = document.getElementById("cancel");
const formCover = document.getElementById("form-cover");
const boughtCover = document.getElementById("bought-cover");

class CoverDisplays {
	// Display the confirm buy form
	displayBuyConfirm() {
		formCover.style.display = "flex";
	}

	// Hide the confirm buy form
	hideBuyConfirm() {
		formCover.style.display = "none";
	}

	// If business has been bought then display confirmation
	displayPurchaseConfirmed() {
		if (bought == true) {
			boughtCover.style.display = "flex";
		}
	}
}

const coverDisplays = new CoverDisplays();
coverDisplays.displayPurchaseConfirmed();

// Add event listeners to buttons
buyButton.addEventListener("click", (e) => {
	coverDisplays.displayBuyConfirm();
});

cancelButton.addEventListener("click", (e) => {
	coverDisplays.hideBuyConfirm();
})
