// Initialize Fabric.js canvas
const canvas = new fabric.Canvas("canvas", {
    width: 960,
    height: 540,
    backgroundColor: "#f0f0f0"
});


// Set default drawing mode to false
canvas.isDrawingMode = false;
// canvas.freeDrawingBrush.width = 2;
// canvas.freeDrawingBrush.color = "black";


// Function to toggle between selection and free drawing mode
function setDrawingMode(enable) {
    canvas.isDrawingMode = enable;
}

// Function to add a rectangle
function addRectangle() {
    const rect = new fabric.Rect({
        left: 50,
        top: 50,
        width: 100,
        height: 60,
        fill: document.getElementById("colorPicker").value,
        stroke: "black",
        strokeWidth: parseInt(document.getElementById("strokeWidth").value)
    });
    canvas.add(rect);
}

// Function to add a circle
function addCircle() {
    const circle = new fabric.Circle({
        left: 100,
        top: 100,
        radius: 50,
        fill: document.getElementById("colorPicker").value,
        stroke: "black",
        strokeWidth: parseInt(document.getElementById("strokeWidth").value)
    });
    canvas.add(circle);
}

// Function to add a line
function addLine() {
    const line = new fabric.Line([50, 200, 250, 200], {
        stroke: document.getElementById("colorPicker").value,
        strokeWidth: parseInt(document.getElementById("strokeWidth").value)
    });
    canvas.add(line);
}

// Function to delete the selected object
function deleteSelected() {
    const activeObject = canvas.getActiveObject();
    if (activeObject) {
        canvas.remove(activeObject);
    }
}

// Function to update object color when selected
document.getElementById("colorPicker").addEventListener("input", function () {
    const activeObject = canvas.getActiveObject();
    if (activeObject) {
        activeObject.set("fill", this.value);
        canvas.renderAll();
    }
});

// Function to update stroke width when selected
document.getElementById("strokeWidth").addEventListener("change", function () {
    const activeObject = canvas.getActiveObject();
    if (activeObject) {
        activeObject.set("strokeWidth", parseInt(this.value));
        canvas.renderAll();
    }
});

// Version 1
// Send vector data to backend
/*
document.getElementById("sendToBackend").addEventListener("click", async () => {
    const jsonData = JSON.stringify({ vector_data: canvas.toJSON() });

    console.log("Sending data to backend:", jsonData);

    try {
        const response = await fetch("http://localhost:8000/receive-sketch/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: jsonData
        });

        const result = await response.json();
        console.log("Response from backend:", result);
    } catch (error) {
        console.error("Error sending data:", error);
    }
});*/


document.getElementById("sendToBackend").addEventListener("click", async () => {
    const textPrompt = prompt("Describe the animation you want:");
    if (!textPrompt) return;

    const jsonData = JSON.stringify({
        vector_json: canvas.toJSON(),
        user_prompt: textPrompt
    });

    console.log("Sending data to backend:", jsonData);

    try {
        const response = await fetch("http://localhost:8000/generate-manim/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: jsonData
        });

        const result = await response.json();
        console.log("Generated Manim Code:", result.manim_code);
        
        alert("Manim code generated! Check console for output.");
    } catch (error) {
        console.error("Error sending data:", error);
    }
});



