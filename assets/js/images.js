/*
 * Images
 */

$(window).on('load', function(){
	$('img').each(function(id, val) {
		let width  = val.naturalWidth;
		let height = val.naturalHeight;
		
		if (height > 150) {
			let newHeight = height * 0.5;
			let newWidth = width * 0.5;
			$(val).height(newHeight);
			$(val).width(newWidth);
			
			$(val).attr("title", $(val).attr ("title") + ": Click to magnify!");
			$(val).css("cursor", "pointer");
			
            let toggled = false;
			$(val).click(function() {
                toggled = !toggled;
                if(toggled) {
                    $(this).stop()
                    $(this).animate({
                        width: width,
                        height: height
                    });
                } else {
                    $(this).stop()
                    $(this).animate({
                        width: (newWidth),
                        height: (newHeight)
                    });
                }
            });
        }
	});
});
