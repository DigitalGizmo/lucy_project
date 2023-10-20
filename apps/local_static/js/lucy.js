htmx.on("htmx:afterSwap", (e) => {
    console.log("inafterSwap, target id: " + e.detail.target.id)
    if (e.detail.target.id == "modal-container") {
        document.getElementById("modal-overlay").classList.remove("hidden");
        // document.getElementById("modal-overlay").classList.add("unhidden");

    }
})

htmx.on("htmx:beforeSwap", (e) => {
    console.log("got to close")
    if (e.detail.target.id == "close-button") {
        document.getElementById("modal-overlay").classList.add("hidden");
    }
})