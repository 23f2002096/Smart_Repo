async function askAI() {

    const input = document.getElementById("question");

    const chat = document.getElementById("chat-box");

    const question = input.value.trim();

    if (!question)
        return;

    chat.innerHTML += `
        <div class="mb-3">
            <strong>You</strong><br>
            ${question}
        </div>
    `;

    input.value = "";

    const response = await fetch(
        "/api/chat",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(
                {
                    question: question
                }
            )
        }
    );

    const data = await response.json();

    chat.innerHTML += `
        <div class="mb-3">
            <strong>Smart Repo</strong><br>
            ${data.answer}
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

}