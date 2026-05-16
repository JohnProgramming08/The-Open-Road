// Fetch data from HTML file
const ownedBusinesses = window.ownedBusinesses || [];
const unownedBusinesses = window.unownedBusinesses || [];
const userID = window.userID;

// Fetch necesary elements
const businessGrid = document.getElementById("business-grid");
const ownedBusinessButton = document.getElementById("owned-businesses-heading");
const unownedBusinessButton = document.getElementById("unowned-businesses-heading");
const categoryButtons = Array.from(document.getElementsByClassName("category"));
const sortButton = document.getElementById("sort-heading");
const businessCards = Array.from(document.getElementsByClassName("business-card"));

// Manage the display of the users businessess
class BusinessDisplay {
	constructor(ownedBusinessData, unownedBusinessData) {
		this.ownedBusinessData = ownedBusinessData;
		this.unownedBusinessData = unownedBusinessData;
		this.displayed = "owned";
		this.lowToHigh = true;
	}

	// Change the bar widths for all owned businesses
	changeBarWidths() {
		for (const business of this.ownedBusinessData) {
			const businessHTML = document.getElementById(String(business.owned_business_id));
			const suppliesBar = Array.from(businessHTML.getElementsByClassName("supplies-bar"))[0];
			const stockBar = Array.from(businessHTML.getElementsByClassName("stock-bar"))[0];

			suppliesBar.style.width = `${business.supplies}%`;
			stockBar.style.width = `${business.stock}%`;
		}
	}

	// Get all of the categories of the displayed businesses
	getDisplayedCategories() {
		let businesses = [];
		if (this.displayed == "owned") {
			businesses = this.ownedBusinessData;
		} else {
			businesses = this.unownedBusinessData;
		}
		
		const categories = [];
		for (const business of businesses) {
			if (!categories.includes(business.type)) {
				categories.push(business.type);
			}
		}

		return categories;
	}

	// Display all the categories of businesses shown
	displayCategories() {
		for (const categoryButton of categoryButtons) {
			if (categoryButton.id != "all") {
				categoryButton.classList.add("hidden");
				categoryButton.classList.remove("selected");
			} else {
				categoryButton.classList.add("selected");
			}
		}

		const categories = this.getDisplayedCategories();
		for (const categoryButton of categoryButtons) {
			if (categories.includes(categoryButton.id)) {
				categoryButton.classList.remove("hidden");
			}
		}
	}

	// Filter displayed businesses by category
	filterByCategory(category) {
		let businesses = [];
		let owned;
		if (this.displayed == "owned") {
			businesses = this.ownedBusinessData;
			owned = true;
		} else {
			businesses = this.unownedBusinessData;
			owned = false;
		}

		// Display all businesses
		if (category == "all") {
			for (const business of businesses) {
				if (owned) {
					const businessHTML = document.getElementById(String(business.owned_business_id));
					businessHTML.style.display = "inline";
				} else {
					const businessHTML = document.getElementById(String(business.business_id));
					businessHTML.style.display = "inline";
				}
			}

			for (const categoryButton of categoryButtons) {
				if (categoryButton.id != "all") {
					categoryButton.classList.remove("selected");
				} else {
					categoryButton.classList.add("selected");
				}
			}
			return 67;
		}

		for (const business of businesses) {
			let businessHTML;
			if (owned) {
				businessHTML = document.getElementById(String(business.owned_business_id));
			} else {
				businessHTML = document.getElementById(String(business.business_id));
			}

			const type = Array.from(businessHTML.getElementsByClassName("type"))[0].getHTML();
			if (type != category) {
				businessHTML.style.display = "none";
			} else {
				businessHTML.style.display = "inline";
			}
		}

		for (const categoryButton of categoryButtons) {
			if (categoryButton.id != category) {
				categoryButton.classList.remove("selected");
			} else {
				categoryButton.classList.add("selected");
			}
		}
	}

	// Display all owned businesses
	displayOwnedBusinesses() {
		for (const business of this.ownedBusinessData) {
			const businessHTML = document.getElementById(String(business.owned_business_id));
			businessHTML.style.display = "inline";
		}

		for (const business of this.unownedBusinessData) {
			const businessHTML = document.getElementById(String(business.business_id));
			businessHTML.style.display = "none";
		}
		this.displayed = "owned";
	}

	// Display all unowned businesses
	displayUnownedBusinesses() {
		for (const business of this.unownedBusinessData) {
			const businessHTML = document.getElementById(String(business.business_id));
			businessHTML.style.display = "inline";
		}

		for (const business of this.ownedBusinessData) {
			const businessHTML = document.getElementById(String(business.owned_business_id));
			businessHTML.style.display = "none";
		}
		this.displayed = "unowned";
	}

	// Swap displays of business buttons
	swapButtonDisplays() {
		if (ownedBusinessButton.classList.contains("selected-heading")) {
			ownedBusinessButton.classList.remove("selected-heading");
			ownedBusinessButton.classList.add("unselected-heading");
			unownedBusinessButton.classList.remove("unselected-heading");
			unownedBusinessButton.classList.add("selected-heading");
		} else {
			unownedBusinessButton.classList.remove("selected-heading");
			unownedBusinessButton.classList.add("unselected-heading");
			ownedBusinessButton.classList.remove("unselected-heading");
			ownedBusinessButton.classList.add("selected-heading");
		}
	}

	// Reverse the order of displayed businesses
	reverseOrder() {
		businessCards.reverse()
		for (const card of businessCards) {
			if (card.classList.contains("unowned")) {
				businessGrid.removeChild(card);
				businessGrid.appendChild(card);
			}
		}

		if (this.lowToHigh) {
			this.lowToHigh = false;
			sortButton.innerHTML = '<p class="orange">Sort: </p> High to Low';
		} else {
			this.lowToHigh = true;
			sortButton.innerHTML = '<p class="orange">Sort: </p> Low to High';
		}
	}
}

// Display all owned businesses when page is loaded
const businessDisplay = new BusinessDisplay(ownedBusinesses, unownedBusinesses);
businessDisplay.changeBarWidths();
businessDisplay.displayOwnedBusinesses();
businessDisplay.displayCategories();
sortButton.style.display = "none";

// Add event listeners to business buttons
ownedBusinessButton.addEventListener("click", (e) => {
	businessDisplay.displayOwnedBusinesses();
	businessDisplay.displayCategories();
	sortButton.style.display = "none";
	if (!(ownedBusinessButton.classList.contains("selected-heading"))) {
		businessDisplay.swapButtonDisplays();
	}
});

unownedBusinessButton.addEventListener("click", (e) => {
	businessDisplay.displayUnownedBusinesses();
	businessDisplay.displayCategories();
	sortButton.style.display = "flex";
	if (!(unownedBusinessButton.classList.contains("selected-heading"))) {
		businessDisplay.swapButtonDisplays();
	}
});

// Add event listeners to category buttons
for (const categoryButton of categoryButtons) {
	categoryButton.addEventListener("click", (e) => {
		businessDisplay.filterByCategory(e.target.id);
	});
}

// Add event listener to sort button
sortButton.addEventListener("click", (e) => {
	businessDisplay.reverseOrder();
});