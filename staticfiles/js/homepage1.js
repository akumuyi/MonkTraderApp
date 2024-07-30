document.addEventListener('DOMContentLoaded', function() {
    const navbarSection = document.getElementById('navbar_section');
    const openNavbarBtn = document.getElementById('open_navbar');
    const closeNavbarBtn = document.getElementById('close_navbar');
    const mainContent = document.getElementById('main_content');

    const overviewLink = document.getElementById('overview_link');
    const marketReportsLink = document.getElementById('market_reports_link');
    const signalServicesLink = document.getElementById('signal_services_link');
    const educationLink = document.getElementById('education_link');

    const overviewSection = document.getElementById('overview_section');
    // const marketReportsSection = document.getElementById('market_reports_section');
    // const signalServicesSection = document.getElementById('signal_services_section');
    // const educationSection = document.getElementById('education_section');

    openNavbarBtn.addEventListener('click', function() {
        navbarSection.classList.add('active');
        mainContent.classList.add('blurred');
    });

    closeNavbarBtn.addEventListener('click', function() {
        navbarSection.classList.remove('active');
        mainContent.classList.remove('blurred');
    });

    function showSection(section) {
        const sections = [overviewSection];
        // const sections = [overviewSection, marketReportsSection, signalServicesSection, educationSection];
        sections.forEach(function(sec) {
            if (sec === section) {
                sec.classList.add('active_section');
                sec.classList.remove('hidden_section');
            } else {
                sec.classList.remove('active_section');
                sec.classList.add('hidden_section');
            }
        });
        mainContent.classList.remove('blurred');
        navbarSection.classList.remove('active');

        // Apply animation
        section.classList.add('ease-in-top');
        setTimeout(() => {
            section.classList.remove('ease-in-top');
        }, 2000);  // Match the duration with the CSS animation duration
    }

    overviewLink.addEventListener('click', function() {
        showSection(overviewSection);
    });

    // marketReportsLink.addEventListener('click', function() {
    //     showSection(marketReportsSection);
    // });

    // signalServicesLink.addEventListener('click', function() {
    //     showSection(signalServicesSection);
    // });

    // educationLink.addEventListener('click', function() {
    //     showSection(educationSection);
    // });

    // Initialize the page to show the overview section by default
    showSection(overviewSection);

    // Handle form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
            }
        });
    });
});