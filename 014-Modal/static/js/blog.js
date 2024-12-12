document.addEventListener("DOMContentLoaded", () => {
    const articles = document.querySelectorAll("article");
    const modal = document.getElementById("modal");
    const modalTitle = document.getElementById("modal-title");
    const modalTime = document.getElementById("modal-time");
    const modalBody = document.getElementById("modal-body");
    const modalClose = document.querySelector(".close");

    articles.forEach((article) => {
        const fullContent = article.querySelector("p").textContent;
        const firstWords = fullContent.split(" ").slice(0, 10).join(" ") + "...";
        article.querySelector("p").textContent = firstWords;

        article.addEventListener("click", () => {
            modalTitle.textContent = article.querySelector("h4").textContent;
            modalTime.textContent = article.querySelector("time").textContent;
            modalBody.textContent = fullContent;
            modal.style.display = "flex";
        });
    });

    modalClose.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});
