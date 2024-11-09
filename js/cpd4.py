document.querySelectorAll('img').forEach(img => {
  img.onerror = function() {
    this.onerror = null; // Prevents infinite loop if default image is also missing
    this.src = 'images/default_image.jpg';
    this.alt = "default image"
  };
});

// Create ScrollTimeline
const myScrollTimeline = new ScrollTimeline({
	source: document.scrollingElement,
	orientation: 'block',
    scrollOffsets: [
        new CSSUnitValue(0, 'percent'),
        new CSSUnitValue(100, 'percent'),
    ],
});

// Animate Progress Bar on Scroll
new Animation(
	new KeyframeEffect(
		document.querySelector('#progress'),
		{
			transform: ['scaleX(0)', 'scaleX(1)'],
		},
		{ duration: 1, fill: "forwards" }
	),
	myScrollTimeline
).play();