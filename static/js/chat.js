const chatBox = document.getElementById("chat-box");
const questionInput = document.getElementById("question");

function scrollToBottom() {
    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: "smooth"
    });
}

function hideEmptyState() {
    const emptyState = document.getElementById("empty-state");

    if (emptyState) {
        emptyState.remove();
    }
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function createUserMessage(question) {

    return `
        <div class="card mb-3 border-0">

            <div class="card-body bg-primary text-white rounded">

                <strong>🧑 You</strong>

                <hr>

                ${escapeHtml(question)}

            </div>

        </div>
    `;
}

function createAssistantMessage(answer) {

    const html = marked.parse(answer);

    return `
        <div class="card mb-3 border-start border-4 border-success">

            <div class="card-body">

                <strong>🤖 Smart Repo</strong>

                <hr>

                <div class="assistant-content">

                    ${html}

                </div>

            </div>

        </div>
    `;
}

function createLoadingMessage() {

    return `
        <div
            id="loading-message"
            class="card mb-3 border-start border-4 border-warning">

            <div class="card-body">

                <strong>🤖 Smart Repo</strong>

                <hr>

                <div class="d-flex align-items-center">

                    <div
                        class="spinner-border spinner-border-sm me-2"
                        role="status">
                    </div>

                    Thinking...

                </div>

            </div>

        </div>
    `;
}

async function askAI() {

    const question = questionInput.value.trim();

    if (!question)
        return;

    hideEmptyState();

    chatBox.insertAdjacentHTML(
        "beforeend",
        createUserMessage(question)
    );

    scrollToBottom();

    questionInput.value = "";

    chatBox.insertAdjacentHTML(
        "beforeend",
        createLoadingMessage()
    );

    scrollToBottom();

    try {

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );

        const data = await response.json();

        document
            .getElementById("loading-message")
            ?.remove();

        if (data.error) {

            chatBox.insertAdjacentHTML(
                "beforeend",
                `
                <div class="alert alert-danger">
                    ${escapeHtml(data.error)}
                </div>
                `
            );

            scrollToBottom();

            return;
        }

        chatBox.insertAdjacentHTML(
            "beforeend",
            createAssistantMessage(data.answer)
        );

        document
            .querySelectorAll("pre code")
            .forEach((block) => {
                hljs.highlightElement(block);
            });

        addCopyButtons();

        scrollToBottom();

    }

    catch (error) {

        document
            .getElementById("loading-message")
            ?.remove();

        chatBox.insertAdjacentHTML(
            "beforeend",
            `
            <div class="alert alert-danger">

                Unable to contact the AI service.

            </div>
            `
        );

        scrollToBottom();
    }
}

function addCopyButtons() {

    document.querySelectorAll("pre").forEach((pre) => {

        if (pre.querySelector(".copy-btn"))
            return;

        const button = document.createElement("button");

        button.className =
            "btn btn-sm btn-outline-secondary copy-btn";

        button.innerHTML = "📋 Copy";

        button.style.float = "right";

        button.onclick = () => {

            navigator.clipboard.writeText(
                pre.innerText
            );

            button.innerHTML = "✅ Copied";

            setTimeout(() => {

                button.innerHTML = "📋 Copy";

            }, 1500);

        };

        pre.prepend(button);

    });

}

questionInput.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Enter") {

            askAI();

        }

    }
);