//* fetch helpers
export const fetchJson = async (url, init = {}) => {
  const res = await fetch(url, init);
  if (!res.ok) {
    throw new Error(`${res.status}: ${await res.text()}`);
  }
  return res.text();
};

export const fetchAndSetAll = async (collection) => {
  const allData = await Promise.all(
    collection.map(({ url, init }) => fetchJson(url, init))
  );

  collection.forEach(({ setter }, i) => {
    setter(allData[i]);
  });
};

//* index
const baseUrl =
  "https://raw.githubusercontent.com/hienerd93/python_structure_algorithm/refs/heads/main/";

const setText = (text) => {
  document.getElementById("text").innerHTML = text;
};

const setEdiot = (text) => {
  document.getElementById("editor").textContent = text;
};

fetchAndSetAll([
  {
    url: baseUrl + "week1/camel_case_4.html",
    setter: setText,
  },
  {
    url: baseUrl + "week1/camel_case_4.py",
    setter: setEdiot,
  },
]).catch(console.error);
