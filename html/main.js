
const updateMap = async () => {
    const response = await fetch('/api/map');
    const data = await response.text();
    document.getElementById("map").innerText = data
}

updateMap()