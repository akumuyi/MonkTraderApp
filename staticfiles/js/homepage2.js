// document.addEventListener("DOMContentLoaded", function () {
//     const navbarSection = document.getElementById("navbar_section");
//     const openBtn = document.getElementById("open_navbar");
//     const closeBtn = document.getElementById("close_navbar");
//     const overviewLink = document.getElementById("overview_link");
//     const marketReportsLink = document.getElementById("market_reports_link");
//     const signalServicesLink = document.getElementById("signal_services_link");
//     const educationLink = document.getElementById("education_link");
//     const manageSubscriptionLink = document.getElementById("manage_subscription_link");
//     const mainContent = document.getElementById("main_content");

//     const overviewSection = document.getElementById("overview_section");
//     const marketReportsSection = document.getElementById("market_reports_section");
//     const signalServicesSection = document.getElementById("signal_services_section");
//     const educationSection = document.getElementById("education_section");
//     const manageSubscriptionSection = document.getElementById("manage_subscription_section");

//     // Function to open the navbar
//     openBtn.addEventListener("click", function () {
//         navbarSection.classList.add("active");
//         mainContent.classList.add("blurred");
//     });

//     // Function to close the navbar
//     closeBtn.addEventListener("click", function () {
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });

//     // Function to show a section and hide othersa
//     function showSection(section) {
//         [overviewSection, marketReportsSection, signalServicesSection, educationSection, manageSubscriptionSection].forEach(sec => {
//             if (sec === section) {
//                 sec.classList.add("active_section");
//                 sec.classList.remove("hidden_section");
//             } else {
//                 sec.classList.add("hidden_section");
//                 sec.classList.remove("active_section");
//             }
//         });
//     }

//     // Event listeners for navbar links
//     overviewLink.addEventListener("click", function () {
//         showSection(overviewSection);
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });

//     marketReportsLink.addEventListener("click", function () {
//         showSection(marketReportsSection);
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });

//     signalServicesLink.addEventListener("click", function () {
//         showSection(signalServicesSection);
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });

//     educationLink.addEventListener("click", function () {
//         showSection(educationSection);
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });

//     manageSubscriptionLink.addEventListener("click", function () {
//         showSection(manageSubscriptionSection);
//         navbarSection.classList.remove("active");
//         mainContent.classList.remove("blurred");
//     });
// });



document.addEventListener('DOMContentLoaded', function() {
    const navbarSection = document.getElementById('navbar_section');
    const openNavbarBtn = document.getElementById('open_navbar');
    const closeNavbarBtn = document.getElementById('close_navbar');
    const mainContent = document.getElementById('main_content');

    const overviewLink = document.getElementById('overview_link');
    const marketReportsLink = document.getElementById('market_reports_link');
    const signalServicesLink = document.getElementById('signal_services_link');
    const educationLink = document.getElementById('education_link');
    const manageSubscriptionLink = document.getElementById('manage_subscription_link');

    const overviewSection = document.getElementById('overview_section');
    const marketReportsSection = document.getElementById('market_reports_section');
    const signalServicesSection = document.getElementById('signal_services_section');
    const educationSection = document.getElementById('education_section');
    const manageSubscriptionSection = document.getElementById('manage_subscription_section');

    openNavbarBtn.addEventListener('click', function() {
        navbarSection.classList.add('active');
        mainContent.classList.add('blurred');
    });

    closeNavbarBtn.addEventListener('click', function() {
        navbarSection.classList.remove('active');
        mainContent.classList.remove('blurred');
    });

    overviewLink.addEventListener('click', function() {
        showSection(overviewSection);
    });

    marketReportsLink.addEventListener('click', function() {
        showSection(marketReportsSection);
    });

    signalServicesLink.addEventListener('click', function() {
        showSection(signalServicesSection);
    });

    educationLink.addEventListener('click', function() {
        showSection(educationSection);
    });

    manageSubscriptionLink.addEventListener('click', function() {
        showSection(manageSubscriptionSection);
    });

    function showSection(section) {
        const sections = [overviewSection, marketReportsSection, signalServicesSection, educationSection, manageSubscriptionSection];
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
    }
});
