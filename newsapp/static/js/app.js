$(function () {
	var $image_containers = $('.article-image-container');
	$image_containers.imagesLoaded(function () {
		$(this).isotope({
			itemSelector: '.article-image',
			cellsByRow: {
    			columnWidth: 1170,
    			rowHeight: 200
  			}
		});
	});
});