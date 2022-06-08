/* global window, document, URLSearchParams */

const url = (new URLSearchParams(window.location.search)).get("url");
const isFiltered = parseInt((new URLSearchParams(window.location.search)).get("is-filtered"));
document.getElementById("url").textContent = url;
document.getElementById("is-filtered").textContent = isFiltered ? ' (Result of filter)' : ' (Result of machine learning)';

const getHostname = (url) => {
    return new URL(url).host
}

const getRules = (blocked) => {
    let rules = blocked.map(item => {
      return {
        isFiltered: item.isFiltered,
        url: getHostname(item.url),
        skip: item.skip ? 1 : 0
      }
    }).sort((a, b) => b.url.length - a.url.length)

    return rules;
  };

document.getElementById('continue').addEventListener("click", () => {
    chrome.storage.local.get("blocked", function (local) {
        const hostname = getHostname(url)
        let block = local.blocked.map((bl => {
            if(getHostname(bl.url) === hostname) {
                bl.skip = 1
            }
            return bl
        }))
        chrome.storage.local.set({ blocked: block }).then(() => {
            document.location.href = url
        });
    });
});