// Deal of the Day Countdown Timer
function initDealCountdowns() {
    // Find all countdown containers
    const countdownContainers = document.querySelectorAll('[data-countdown]');

    if (countdownContainers.length === 0) {
        console.log('No countdown containers found');
        return;
    }

    countdownContainers.forEach(function(container, index) {
        const endTimeStr = container.getAttribute('data-countdown');

        if (!endTimeStr) {
            console.log('No end time for container', index);
            return;
        }

        const endTime = parseInt(endTimeStr);

        console.log('Setting up countdown', index, 'End time:', new Date(endTime));

        // Get the countdown elements within this specific container
        const daysEl = container.querySelector('.days');
        const hoursEl = container.querySelector('.hours');
        const minutesEl = container.querySelector('.minutes');
        const secondsEl = container.querySelector('.seconds');

        if (!daysEl || !hoursEl || !minutesEl || !secondsEl) {
            console.log('Missing countdown elements in container', index);
            return;
        }

        // Update countdown every second
        function updateCountdown() {
            const now = new Date().getTime();
            const distance = endTime - now;

            // If countdown is finished
            if (distance < 0) {
                daysEl.innerHTML = '<span>0</span><p>D</p>';
                hoursEl.innerHTML = '<span>0</span><p>H</p>';
                minutesEl.innerHTML = '<span>0</span><p>M</p>';
                secondsEl.innerHTML = '<span>0</span><p>S</p>';
                return;
            }

            // Calculate time units
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            // Update the display
            daysEl.innerHTML = '<span>' + days + '</span><p>D</p>';
            hoursEl.innerHTML = '<span>' + hours + '</span><p>H</p>';
            minutesEl.innerHTML = '<span>' + minutes + '</span><p>M</p>';
            secondsEl.innerHTML = '<span>' + seconds + '</span><p>S</p>';
        }

        // Initial update
        updateCountdown();

        // Update every second
        setInterval(updateCountdown, 1000);
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        // Wait a bit for Slick carousel to initialize
        setTimeout(initDealCountdowns, 500);
    });
} else {
    // DOM already loaded
    setTimeout(initDealCountdowns, 500);
}

// Also try to reinitialize after Slick carousel events
$(document).ready(function() {
    $('#deal_of_day').on('init', function() {
        console.log('Slick initialized, starting countdowns');
        initDealCountdowns();
    });

    $('#deal_of_day').on('afterChange', function() {
        initDealCountdowns();
    });
});