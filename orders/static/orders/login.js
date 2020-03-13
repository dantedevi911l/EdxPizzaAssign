document.addEventListener('DOMContentLoaded', () => {

	document.querySelector(".sign-up").classList.add("invisible");

	var signup = document.querySelector(".sign-up-button");
	signup.addEventListener("click" , function() {
		document.querySelector(".sign-in").classList.add("invisible");
		document.querySelector(".sign-up").classList.remove("invisible");
		document.querySelector(".sign-up").classList.add("visible");
	});

});
