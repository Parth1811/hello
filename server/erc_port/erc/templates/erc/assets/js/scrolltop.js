// ===== Scroll to Top ==== 
$(window).scroll(function() {
    if ($(this).scrollTop() >= $('.entry-title').position().top) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});

function scrollback() {
	$('html, body').animate({
		scrollTop: $("#main").offset().top
	}, 500);
	/*
	if($(".entry-feature-image").length){
		$('html, body').animate({
			scrollTop: ($("#main").offset().top+200)
		}, 500);
	} 
	*/
};