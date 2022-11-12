/*
 * News
 */

$(function(){   
	$('#news dd').each(function () {
		$(this).hide();
	});
	
	$('#news dt a').each(function () {
		var title = $(this).attr('title');
		$(this).attr('title', title + ', Click to toggle');
	});
	
	$('#news dt a').click(function () {
		$(this).parent().next().slideToggle();
        return false;
	});
});
