document.addEventListener("DOMContentLoaded", function () {
    fetchTasks();

    document.getElementById("taskForm").addEventListener("submit", function (e) {
        e.preventDefault();
        const title = document.getElementById("taskInput").value.trim();

        if (title) {
            console.log("Submitting task:", title);
            addTask(title);
            document.getElementById("taskInput").value = "";
        } else {
            console.warn("❌ Task input is empty.");
        }
    });

    document.getElementById("deleteAllBtn").addEventListener("click", deleteAllTasks);
});

function fetchTasks() {
    fetch("https://todo-app-1-j941.onrender.com")
        .then(response => response.json())
        .then(data => {
            console.log("Fetched tasks:", data);
            const taskList = document.getElementById("taskList");
            taskList.innerHTML = "";

            data.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.title;

                const delBtn = document.createElement("button");
                delBtn.textContent = "❌";
                delBtn.onclick = () => deleteTask(task.id);

                li.appendChild(delBtn);
                taskList.appendChild(li);
            });
        })
        .catch(error => console.error("❌ Error fetching tasks:", error));
}

function addTask(title) {
    fetch("https://todo-app-1-j941.onrender.com", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ task_title: title })  // Must match backend key
    })
    .then(response => response.json())
    .then(data => {
        console.log("✅ Server response:", data);
        fetchTasks();
    })
    .catch(error => {
        console.error("❌ Error submitting task:", error);
    });
}

function deleteTask(id) {
    fetch(`https://todo-app-1-j941.onrender.com${id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        console.log("🗑️ Deleted task:", data);
        fetchTasks();
    })
    .catch(error => console.error("❌ Error deleting task:", error));
}

function deleteAllTasks() {
    fetch("https://todo-app-1-j941.onrender.com", {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        console.log("🧹 All tasks deleted:", data);
        fetchTasks();
    })
    .catch(error => console.error("❌ Error deleting all tasks:", error));
}
