
const updateMap = async () => {
    const response = await fetch('/api/map');
    const data = await response.text();
    document.getElementById("map").innerText = data
}

const post = async (endpoint, body) => {
    return fetch(endpoint, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    })
}

const login = async () => {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    response = await post('/api/login', {
        username: username,
        password: password
    })

    if (! response.ok) {
        alert(response.statusText)
    } else {
        alert("Successfully logged in")
    }
}


const register = async () => {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    response = await post('/api/register', {
        username: username,
        password: password
    })

    if (! response.ok) {
        alert(response.statusText)
    } else {
        alert("Successfully registerd")
    }
}


updateMap()