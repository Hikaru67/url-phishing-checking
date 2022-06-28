"use strict";

/* global chrome, window, document */
var blockedUrls = [];
var blockedStorage = [];
const blockedList = document.getElementById("blocked-list");
const resolutionSelect = document.getElementById("resolution-select");
const enabledToggle = document.getElementById("enabled-toggle");

const addButton = document.getElementById("btn-add");
const clearButton = document.getElementById("btn-clear");
const clearAllButton = document.getElementById("btn-clear-all");

blockedList.placeholder = [
  "facebook.com",
  "instagram.com",
  "youtube.com",
  "!music.youtube.com",
  "twitter.com",
  "reddit.com",
  "!reddit.com/r/MachineLearning",
].join("\n");

enabledToggle.addEventListener("change", (event) => {
  const enabled = event.target.checked;

  chrome.storage.local.set({ enabled });
});

function initStorage() {
  chrome.storage.local.get(["enabled", "blocked", "resolution"], function (local) {
    let { enabled, blocked } = local;
    if (!Array.isArray(blocked)) {
      return;
    }
    blockedStorage = JSON.parse(JSON.stringify(blocked))
    console.log('🚀 ~ local', local)

    // blocked
    blocked = blocked.map(bl => {
      blockedUrls[bl.url] = 1
      return bl.url
    })
    var value = blocked.join("\r\n"); // display every blocked in new line
    blockedList.value = value;

    // enabled
    enabledToggle.checked = enabled;

    // UI ready
    document.body.classList.add("ready");
  });
}

window.addEventListener("DOMContentLoaded", initStorage());

addButton.addEventListener("click", async (event) => {
  const reg = new RegExp(/^(http(s?):\/\/)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)/)
  const url = document.getElementById('url').value
  if (!reg.test(url)){
    alert('Url không hợp lệ')
    return
  }
  if (blockedUrls[url]) {
    alert('Url đã tồn tại')
    return
  }
  await setBlockList(url)
});

clearButton.addEventListener("click", async (event) => {
  const reg = new RegExp(/^(http(s?):\/\/)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)/)
  const url = document.getElementById('url').value
  if (!reg.test(url)){
    alert('Url không hợp lệ')
    return
  }
  if (!blockedUrls[url]) {
    alert('Thêm url trước khi nhấn nút xóa!')
    return
  }
  const conf = confirm('Bạn chắc chắn chứ?!')
  if (!conf) { return }

  blockedUrls[url] = 0
  delete blockedUrls[url]
  blockedStorage = deleteElementInArray(blockedStorage, url)
  await chrome.storage.local.set({ blocked: blockedStorage })
  initStorage()
});

clearAllButton.addEventListener("click", async () => {
  const conf = confirm('Bạn đang tỉnh đấy chứ?!')
  if (!conf) { return }

  blockedStorage = []
  blockedUrls = []
  await chrome.storage.local.set({ blocked: blockedStorage })
  initStorage()
})

async function setBlockList(url) {
  if (!url || blockedUrls[url]) { return }

  blockedStorage.push({
    url,
    isFiltered: 1
  })
  await chrome.storage.local.set({ blocked: blockedStorage })
  initStorage()
}

function deleteElementInArray(queryData, url) {
  let index = 0
  queryData.find(item => {
    if (item.url === url) {
      return url
    }
    index++
  })
  const newQueryData = queryData.slice(0, index)
  queryData = queryData.splice(index + 1, queryData.length)
  queryData.forEach(item => {
    newQueryData.push(item)
  })

  return newQueryData
}