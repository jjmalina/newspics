$(function () {
	var $image_containers = $('.article-image-container');
	$image_containers.imagesLoaded(function () {
		$(this).isotope({
			itemSelector: '.article-image',
			masonry: {
				columnWidth: 350
			}
		});
	});

	$(".article-image a").live('click', function () {
		$.fancybox({ 'href': $(this).attr('href') });
		return false;
	});
});