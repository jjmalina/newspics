$(function () {
	var $image_containers = $('.article-image-container');
	$image_containers.imagesLoaded(function () {
		$(this).isotope({
			itemSelector: '.article-image',
			masonry: {
				columnWidth: 1120
			}
		});
	});
});