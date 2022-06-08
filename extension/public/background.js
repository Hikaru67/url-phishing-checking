"use strict";

/* global chrome */

const CLOSE_TAB = "CLOSE_TAB";
const SHOW_BLOCKED_INFO_PAGE = "SHOW_BLOCKED_INFO_PAGE";

const RESOLUTIONS = [
  CLOSE_TAB,
  SHOW_BLOCKED_INFO_PAGE,
];

chrome.runtime.onInstalled.addListener(function () {
  chrome.storage.local.get(["enabled", "blocked", "resolution"], function (local) {
    if (typeof local.enabled !== "boolean") {
      chrome.storage.local.set({ enabled: false });
    }

    if (!Array.isArray(local.blocked)) {
      let list = []
      chrome.storage.local.set({ blocked: [] });
    }

    if (!RESOLUTIONS.includes(local.resolution)) {
      chrome.storage.local.set({ resolution: CLOSE_TAB });
    }
  });
});

const __removeProtocol = (url) => url.replace(/^http(s?):\/\//, "");
const __removeWww = (url) => url.replace(/^www\./, "");
const __removeTrailingSlash = (url) => url.endsWith("/") ? url.slice(0, -1) : url;

// "https://www.youtube.com/" => "youtube.com"
// "https://www.youtube.com/feed/explore" => "youtube.com/feed/explore"
// "https://music.youtube.com/" => "music.youtube.com"
// "https://music.youtube.com/explore" => "music.youtube.com/explore"
const normalizeUrl = (url) => [url]
  .map(__removeProtocol)
  .map(__removeWww)
  .map(__removeTrailingSlash)
  .pop();

const getHostname = (url) => {
  try {
    return new URL(url).hostname
  } catch (error) {
    return url
  }
}

// ["youtube.com", "!music.youtube.com"] => [{ path: "music.youtube.com", type: "allow" }, { path: "youtube.com", type: "block" }]
// ["https://youtube.com/", "!https://music.youtube.com/"] => [{ path: "music.youtube.com", type: "allow" }, { path: "youtube.com", type: "block" }]
const getRules = (blocked) => {
  let rules = blocked.map(item => {
    return {
      isFiltered: item.isFiltered,
      url: getHostname(item.url),
      skip: item.skip ? 1 : 0
    }
  })
  // const allowList = blocked
  //   .filter((item) => item.startsWith("!"))
  //   .map((item) => normalizeUrl(item.substring(1)));

  // const blockList = blocked
  //   .filter((item) => !item.url.startsWith("!"))
  //   .map(normalizeUrl);

  //  rules = [
  //   ...allowList.map((path) => ({ path, type: "allow" })),
  //   ...blockList.map((path) => ({ path, type: "block" })),
  // ].sort((a, b) => b.path.length - a.path.length); // order the rules by their specificity; the longer the rule, the more specific

  return rules;
};

chrome.tabs.onUpdated.addListener(function (tabId, changeInfo) {
  const url = changeInfo.pendingUrl || changeInfo.url;
  if (!url || !url.startsWith("http")) {
    return;
  }

  const hostname = getHostname(url);

  chrome.storage.local.get(["enabled", "blocked", "resolution"], function async (local) {
    let { enabled, blocked } = local;
    if (!enabled || !Array.isArray(blocked) || blocked.length === 0) {
      return;
    }
    
    const foundRule = blocked.find((bl => getHostname(bl.url) === hostname));
    console.log('🚀 ~ u', u)
    if (!foundRule) {
      fetch('http://127.0.0.1:8000/api/url-phishing-checking', {
        method: 'POST',
        body: { url: url }
      }).then(response => response.json())
        .then(data => {
          console.log(data.data)
        })
    }
    if (!foundRule || foundRule.skip) {
      return;
    }

    chrome.tabs.update(tabId, { url: `${chrome.runtime.getURL("blocked.html")}?url=${url}&is-filtered=${foundRule.isFiltered}` });
  });
});

const phishingChecking = async (url) => {
  const response = await fetch('http://127.0.0.1:8000/api/url-phishing-checking', {
    method: 'POST',
    body: { url: url }
  })
  console.log('🚀 ~ response', response)
}
        // .then(response => response.json())
        // .then(data => {
        //   list = data.data
        //   list = list.map(item => {
        //     if (item.url[item.url.length - 1] === '\n') {
        //       item.url = item.url.substring(0, item.url.length - 1)
        //     }
        //     return {
        //       url: item.url,
        //       isFiltered: 1
        //     }
        //   })
        // })