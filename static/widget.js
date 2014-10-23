(function() {
  var el, iframe;
  el = document.getElementById('widget');
  iframe = document.createElement('iframe');
  iframe.setAttribute('src', el.href + "/widget");
  iframe.setAttribute('width', '300');
  iframe.setAttribute('height', '240');
  iframe.setAttribute('frameborder', '0');
  iframe.setAttribute('scrolling', 'no');
  el.parentNode.replaceChild(iframe, el);
})();
