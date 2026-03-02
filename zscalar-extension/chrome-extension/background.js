// Listen for messages from the content script and forward to native host
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "launch_edge") {
    chrome.runtime.sendNativeMessage(
      "com.zsa.launcher",
      { url: message.zsaUrl },
      (response) => {
        if (chrome.runtime.lastError) {
          sendResponse({ success: false, error: chrome.runtime.lastError.message });
        } else {
          sendResponse({ success: true, response });
        }
      }
    );
    return true; // keep channel open for async sendResponse
  }
});
