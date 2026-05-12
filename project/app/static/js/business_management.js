// Fetch data from HTML file
const summaryData = window.summaryData;
const upgradesData = window.upgradesData;

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

class SectionDisplay {
	constructor(summary, upgrades) {
		this.summaryData = summary;
		this.upgradesData = upgrades;
	}

	// Make a button unclickable
	restrictButton(button) {
		button.style.cursor = "auto";
		button.style.background = "grey";
		button.onclick = null;
	}

	// Runs at page load, restricts all buttons which should be unclickable
	restrictButtons() {
		// Business hasn't been set up
		if (!this.summaryData.setup_started) {
			this.restrictButton(upgradesButton);
			this.restrictButton(sellButton);
		}
		// Business is being set up
		if (this.summaryData.setup_started && !this.summaryData.setup_finished) {
			this.restrictButton(setupButton);
			this.restrictButton(upgradesButton);
			this.restrictButton(sellButton);
		}
		// Business has been setup
		if (this.summaryData.setup_finished) {
			setupButton.style.display = "none";
		}
		// Supplies are being delivered
		if (this.summaryData.supplies_bought) {
			this.restrictButton(upgradesButton);
		}
		// Sale is being made
		if (this.summaryData.sale_started) {
			this.restrictButton(sellButton);
		}
	}
}

const display = new SectionDisplay(summaryData, upgradesData);
display.restrictButtons(0);

// Add resupply button to HTML and the resupply section to HTML and CSS and JS