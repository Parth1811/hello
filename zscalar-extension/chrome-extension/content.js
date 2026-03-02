(() => {
  function buildZsaUrl() {
    const queryString = window.location.search.substring(1);
    return queryString ? `zsa://token?${queryString}` : "zsa://token";
  }

  function injectButton() {
    if (document.getElementById("zsa-parallels-btn")) return;

    // Find the existing "Launch" button
    const launchBtn = document.getElementById("button");
    if (!launchBtn) return;

    const btn = document.createElement("div");
    btn.id = "zsa-parallels-btn";
    btn.textContent = "Launch in Parallels";
    btn.tabIndex = 0;
    btn.title = "Launch Microsoft Edge in Parallels with the ZSA token";

    btn.style.cssText = `
      margin-top: 15px;
      background-color: #1c508c;
      font-size: 16px;
      border-radius: 4px;
      color: white;
      padding: 15px;
      border: none;
      width: 100px;
      text-align: center;
      margin-left: auto;
      margin-right: auto;
      cursor: pointer;
    `;

    btn.addEventListener("click", handleClick);
    btn.addEventListener("keypress", (e) => { if (e.keyCode === 13) handleClick(); });

    // Insert right after the Launch button
    launchBtn.insertAdjacentElement("afterend", btn);
  }

  function handleClick() {
    const btn = document.getElementById("zsa-parallels-btn");
    const zsaUrl = buildZsaUrl();
    btn.textContent = "Launching...";
    btn.style.pointerEvents = "none";
    btn.style.opacity = "0.6";

    chrome.runtime.sendMessage(
      { type: "launch_edge", zsaUrl },
      (resp) => {
        if (resp && resp.success) {
          btn.textContent = "Launched!";
        } else {
          btn.textContent = "Failed — check native host";
          console.error("ZSA Launcher error:", resp?.error);
        }
        setTimeout(() => {
          btn.textContent = "Launch in Parallels";
          btn.style.pointerEvents = "";
          btn.style.opacity = "";
        }, 3000);
      }
    );
  }

  injectButton();
})();
