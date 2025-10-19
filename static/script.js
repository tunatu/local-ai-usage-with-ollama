const sr = "https://media.tenor.com/lUIQnRFbpscAAAAi/loading.gif";

async function trig(event) {
    event.preventDefault(); // stop form from reloading

    const imge = document.getElementById("gid");
    imge.src = sr; // show loading GIF

    const form = document.querySelector("form");
    const formData = new FormData(form);

    // ✅ Always use the same <pre> element
    let responseBox = document.querySelector("pre");
    if (!responseBox) {
        responseBox = document.createElement("pre");
        document.querySelector(".mainwindow").appendChild(responseBox);
    }

    // ✅ Clear old text before starting a new request
    responseBox.textContent = "";

    try {
        const response = await fetch("/", {
            method: "POST",
            body: formData,
        });

        if (!response.ok || !response.body) {
            responseBox.textContent = "Error: No response from server.";
            imge.src = "";
            return;
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { value, done } = await reader.read();
            if (done) break;
            responseBox.textContent += decoder.decode(value);
            responseBox.scrollTop = responseBox.scrollHeight;
        }
    } catch (error) {
        responseBox.textContent = "Request failed: " + error;
    } finally {
        imge.src = ""; // hide loading GIF after done
    }
}
function trog() {
    let texo = document.getElementsByClassName("warnt")[0];
    texo.style.display = "none"; // hides the div completely, including border
}