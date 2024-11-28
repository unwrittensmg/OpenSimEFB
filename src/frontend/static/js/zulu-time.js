function updateZuluTime() {
    const zuluElement = document.getElementById("zulu-time");
    const now = new Date();
    const zuluTime = now.toISOString().split("T")[1].split(".")[0] + " Zulu";
    zuluElement.textContent = zuluTime;
}

// Refresh time each second
setInterval(updateZuluTime, 1000);

// Initial call
updateZuluTime();
