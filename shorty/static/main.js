function copyResultURL() {
    var el = document.getElementById('result-url');
    navigator.clipboard.writeText(el.innerHTML);
}