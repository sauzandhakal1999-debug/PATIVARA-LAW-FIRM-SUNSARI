/**
 * Pathivara Law Firm Itahari - Accessible Vanilla JavaScript
 * Zero third-party dependencies, high performance, WCAG AA accessible
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Accessible Mobile Navigation Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', function () {
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
      mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
      navLinks.classList.toggle('active');

      if (!isExpanded) {
        navLinks.querySelector('a')?.focus();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navLinks.classList.contains('active')) {
        navLinks.classList.remove('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.focus();
      }
    });
  }

  // 2. Interactive Legal Contact & Consultation Form Handler
  const forms = document.querySelectorAll('form[data-validate="true"]');

  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const statusBox = form.querySelector('.form-status');
      const submitBtn = form.querySelector('button[type="submit"]');
      const nameInput = form.querySelector('[name="client_name"]');
      const contactInput = form.querySelector('[name="contact_info"]');
      const messageInput = form.querySelector('[name="legal_inquiry"]');
      const consentInput = form.querySelector('[name="ethics_consent"]');

      // Basic validation
      if (!nameInput || !nameInput.value.trim()) {
        showStatus(statusBox, 'Please provide your full name.', 'error');
        nameInput?.focus();
        return;
      }

      if (!contactInput || !contactInput.value.trim()) {
        showStatus(statusBox, 'Please provide a valid phone number or email address.', 'error');
        contactInput?.focus();
        return;
      }

      if (!messageInput || !messageInput.value.trim()) {
        showStatus(statusBox, 'Please outline your general legal matter (avoid sensitive confidential specifics).', 'error');
        messageInput?.focus();
        return;
      }

      if (consentInput && !consentInput.checked) {
        showStatus(statusBox, 'Please acknowledge the legal consultation disclaimer before proceeding.', 'error');
        consentInput.focus();
        return;
      }

      // Simulate sending inquiry
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Transmitting Enquiry...';
      }

      setTimeout(function () {
        showStatus(
          statusBox,
          'Your preliminary consultation enquiry has been recorded. Our chambers coordinator will review your request during business hours (Mon–Fri, 9:30 AM–5:00 PM NPT) to confirm advocate availability. Note: Formal advocate-client representation requires execution of a Vakalatnama.',
          'success'
        );
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Submit Legal Enquiry';
        }
      }, 700);
    });
  });

  function showStatus(box, text, type) {
    if (!box) return;
    box.className = 'form-status ' + type;
    box.textContent = text;
    box.style.display = 'block';
    box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
});
