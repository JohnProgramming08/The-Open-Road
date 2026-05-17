// Fetch data from HTML file
const summaryData = window.summaryData;
const upgradesData = window.upgradesData;
const prevButtonClicked = window.buttonClicked;
const userMoney = window.money;
console.log(userMoney);

// Fetch all the necessary DOM elements
const setupButton = document.getElementById("set-up");
const upgradesButton = document.getElementById("buy-upgrades");
const earningsSalesDiv = document.getElementById("earnings-sales-div");
const summaryDiv = document.getElementById("summary-div");
const upgradesDiv = document.getElementById("upgrades-div");
const sellDiv = document.getElementById("sell-div");
const sellButton = document.getElementById("sell-button");
const stockBar = document.getElementById("stock");
const suppliesBar = document.getElementById("supplies");
const resupplyButton = document.getElementById("resupply");
const screenCover = document.getElementById("screen-cover");
const coverText = document.getElementById("cover-text");
const buttonClicked = document.getElementById("button-clicked");
const distance = document.getElementById("distance");
const locationEl = document.getElementById("location");
const form = document.querySelector("form");
const okButton = document.getElementById("ok");
const buyUpgradeButtons = Array.from(document.getElementsByClassName("upgrade"));
const cancelButton = document.getElementById("cancel");
const upgradeStaffButton = document.getElementById("staff-upgrade");
const upgradeEquipmentButton = document.getElementById("equipment-upgrade");
const upgradeSecurityButton = document.getElementById("security-upgrade");
const upgradeDescriptions = Array.from(document.getElementsByClassName("upgrade-description"));
const farLocationDisplay = document.getElementById("far-location");
const closeLocationDisplay = document.getElementById("close-location");
const farBuyerDisplay = document.getElementById("far-company");
const closeBuyerDisplay = document.getElementById("close-company");
const farSaleButton = document.getElementById("far-sell");
const closeSaleButton = document.getElementById("close-sell");
const main = document.querySelector("main");

class SectionDisplay {
	constructor(summary, upgrades, prevButton) {
		this.summaryData = summary;
		this.upgradesData = upgrades;
		this.prevButtonClicked = prevButton;
	}

	// Make a button unclickable
	restrictButton(button) {
		button.style.cursor = "auto";
		button.style.background = "grey";
		button.classList.add("restricted");
		button.onclick = null;
	}

	// Runs at page load, restricts all buttons which should be unclickable
	restrictButtons() {
		// Business hasn't been set up
		if (!this.summaryData.setup_started) {
			this.restrictButton(upgradesButton);
			this.restrictButton(sellButton);
			resupplyButton.style.display = "none";
			console.log("business not setup");
		}
		// Business is being set up
		if (this.summaryData.setup_started && !this.summaryData.setup_finished) {
			this.restrictButton(setupButton);
			this.restrictButton(upgradesButton);
			this.restrictButton(sellButton);
			resupplyButton.style.display = "none";
			console.log("business being setup");
		}
		// Business has been setup
		if (this.summaryData.setup_finished && this.summaryData.setup_started) {
			setupButton.style.display = "none";
			console.log("business has been setup");
		}
		// Supplies are being delivered
		if (this.summaryData.supplies_bought) {
			this.restrictButton(resupplyButton);
			console.log("supplies are being delivered");
		}
		// Sale is being made
		if (this.summaryData.sale_started) {
			this.restrictButton(sellButton);
			console.log("sale is being made");
		}

		// Upgrades already bought
		if (upgradesData.staff_bought) {
			this.restrictButton(upgradeStaffButton);
			upgradeStaffButton.style.cursor = "pointer";
		} if (upgradesData.security_bought) {
			this.restrictButton(upgradeSecurityButton);
			upgradeSecurityButton.style.cursor = "pointer";
		} if (upgradesData.equipment_bought) {
			this.restrictButton(upgradeEquipmentButton);
			upgradeEquipmentButton.style.cursor = "pointer";
		}
	}

	// Show the setup business form to the user
	setupBusinessForm() {
		screenCover.style.display = "flex";
		form.style.display = "flex";
		okButton.style.display = "none";
		coverText.innerHTML = "Are you sure you want to set up this buisness?";
		buttonClicked.value = "setup";
	}

	// Check if there was a last button pressed and if so change text, runs when HTML file loaded
	// Still needs finishing
	wasButtonPressed() {
		if (this.prevButtonClicked == "") {
			return 67
		}

		form.style.display = "none";
		screenCover.style.display = "flex";
		okButton.style.display = "flex";
		
		if (this.prevButtonClicked == "setup") {
			coverText.innerHTML = "Your business is being set up.";
		}

		if (this.prevButtonClicked == "staff" || this.prevButtonClicked == "security" || this.prevButtonClicked == "equipment") {
			coverText.innerHTML = "The upgrade has been purchased.";
		}

		if (this.prevButtonClicked == "resupply") {
			coverText.innerHTML = "A resupply mission has been started";
		}

		if (this.prevButtonClicked == "sell") {
			coverText.innerHTML = "Your sale is currently in progress.";
		}
	}

	// Change the width of the bars 
	changeBarWidths() {
		stockBar.style.width = `${summaryData.stock_level}%`;
		suppliesBar.style.width = `${summaryData.supplies_level}%`;
	}

	// Display the upgrade section
	displayUpgradeSection() {
		upgradesDiv.style.display = "flex";
		earningsSalesDiv.style.display = "none";
		summaryDiv.style.display = "none";
		sellDiv.style.display = "none";
		sellButton.style.display = "flex";
	}

	// Display the buy upgrade form
	buyUpgradeForm(upgrade) {
		// Ensure user has enough money for upgrade
		let price;
		if (upgrade == "staff") {
			price = upgradesData.staff_price;
		} else if (upgrade == "security") {
			price = upgradesData.security_price;
		} else {
			price = upgradesData.equimpent_price;
		}
		if (userMoney < price) {
			screenCover.style.display = "flex";
			form.style.display = "none";
			okButton.style.display = "flex";
			coverText.innerHTML = "You do not have enough for this upgrade.";
			return 67
		}

		screenCover.style.display = "flex";
		form.style.display = "flex";
		okButton.style.display = "none";
		coverText.innerHTML = "Are you sure you would like to buy this upgrade?";
		buttonClicked.value = upgrade;
	}

	// Display the upgrade owned pop-up
	upgradeOwned() {
		screenCover.style.display = "flex";
		form.style.display = "none";
		okButton.style.display = "flex";
		coverText.innerHTML = "You already own this upgrade.";
	}

	// Display the resupply form
	resupplyForm() {
		screenCover.style.display = "flex";
		form.style.display = "flex";
		okButton.style.display = "none";
		coverText.innerHTML = "Would you like to start a resupply mission?";
		buttonClicked.value = "resupply";
	}

	// Display the sell section
	displaySellSection() {
		sellDiv.style.display = "flex";
		earningsSalesDiv.style.display = "none";
		summaryDiv.style.display = "none";
		upgradesDiv.style.display = "none";
		sellButton.style.display = "none";
	}

	// Adjust the sale locations 
	adjustSaleLocations() {
		const locations = {
			"Los Santos": [
				"Elysian Island",
				"Textile City",
				"Downtown Vinewood",
				"Cypress Flats",
				"Vespucci Canals",
				"Terminal",
				"El Burro Heights",
				"Morningwood"
			],
			"Blaine County": [
				"Grapeseed",
				"Paleto Bay",
				"San Chianski Mountain Range",
				"Mount Chiliad",
				"Grand Senora Desert",
				"Alamo Sea"
			]
		};
		const businessLocation = this.summaryData.location;
		
		let farLocation;
		let closeLocation;
		if (locations["Los Santos"].includes(businessLocation)) {
			const farIndex = Math.floor(Math.random() * 5)
			const closeIndex = Math.floor(Math.random() * 7)
			farLocation = locations["Blaine County"][farIndex];
			closeLocation = locations["Los Santos"][closeIndex];
			this.farSaleLocation = "blaine_county";
			this.closeSaleLocation = "los_santos";
		} else {
			const farIndex = Math.floor(Math.random() * 7)
			const closeIndex = Math.floor(Math.random() * 5)
			farLocation = locations["Los Santos"][farIndex];
			closeLocation = locations["Blaine County"][closeIndex];
			this.closeSaleLocation = "blaine_county";
			this.farSaleLocation = "los_santos";
		}

		farLocationDisplay.innerHTML = farLocation;
		closeLocationDisplay.innerHTML = closeLocation;
	}

	// Change the companies buying the sale
	adjustSaleBuyers() {
		const buyers = [
			"Pacific Rim Finance",
			"FoxHen Enterprises Ltd",
			"Redwood Holdings",
			"Tavish & Co.",
			"Brute Force Solutions",
			"Krapea",
			"PostOp",
			"GoPostal",
			"Bilgeco Shipping",
			"Shark Credit Holdings"
		];
		const closeIndex = Math.floor(Math.random() * 9)
		let farIndex = Math.floor(Math.random() * 9);
		while (farIndex == closeIndex) {
			farIndex = Math.floor(Math.random() * 9);
		}

		const closeBuyer = buyers[closeIndex];
		const farBuyer = buyers[farIndex];
		closeBuyerDisplay.innerHTML = closeBuyer;
		farBuyerDisplay.innerHTML = farBuyer;
	}

	// Display the sale form
	displaySaleForm(saleDistance, saleLocation) {
		screenCover.style.display = "flex";
		form.style.display = "flex";
		okButton.style.display = "none";
		coverText.innerHTML = "Are you sure you would like to start a sale?";
		distance.value = saleDistance;
		locationEl.value = saleLocation;
		buttonClicked.value = "sell";
	}

	// Display the standard sections
	displayNormalSections() {
		upgradesDiv.style.display = "none";
		sellDiv.style.display = "none";
		earningsSalesDiv.style.display = "flex";
		summaryDiv.style.display = "flex";
		sellButton.style.display = "flex";
	}
}

const display = new SectionDisplay(summaryData, upgradesData, prevButtonClicked);
display.restrictButtons();
display.wasButtonPressed();
display.changeBarWidths();

// Add button event listeners
if (!setupButton.classList.contains("restricted")) {
	setupButton.addEventListener("click", (e) => {
		display.setupBusinessForm();
	});
}

okButton.addEventListener("click", (e) => {
	screenCover.style.display = "none";
});

upgradesButton.addEventListener("click", (e) => {
	if (!upgradesButton.classList.contains("restricted")) {
		display.displayUpgradeSection();
	}
});

for (const button of buyUpgradeButtons) {
	button.addEventListener("click", (e) => {
		const upgradeButton = Array.from(button.getElementsByClassName("upgrade-button"))[0];
		if (!upgradeButton.classList.contains("restricted")) {
			display.buyUpgradeForm(button.id);
		} else {
			display.upgradeOwned();
		}
	});
}

cancelButton.addEventListener("click", (e) => {
	screenCover.style.display = "none";
})

for (const description of upgradeDescriptions) {
	description.style.opacity = "0";
	description.addEventListener("mouseover", (e) => {
		description.style.opacity = "1";
	});
	description.addEventListener("mouseleave", (e) => {
		description.style.opacity = "0";
	});
}

resupplyButton.addEventListener("click", (e) => {
	if (!resupplyButton.classList.contains("restricted")) {
		display.resupplyForm();
	}
});

sellButton.addEventListener("click", (e) => {
	if (!sellButton.classList.contains("restricted") && summaryData.stock_level > 0) {
		display.displaySellSection();
		display.adjustSaleLocations();
		display.adjustSaleBuyers();
	}
});

farSaleButton.addEventListener("click", (e) => { 
	if (!farSaleButton.classList.contains("restricted")) {
		display.displaySaleForm("far", display.farSaleLocation);
	}
});

closeSaleButton.addEventListener("click", (e) => {
	if (!closeSaleButton.classList.contains("restricted")) {
		display.displaySaleForm("close", display.closeSaleLocation);
	}
});

main.addEventListener("click", (e) => {
	if (!e.target.classList.contains("button")) {
		display.displayNormalSections();
	}
});