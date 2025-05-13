<footer class="footer mt-auto py-3 bg-light">
  <div class="container">
      <div class="row">
          <div class="col-md-4">
              <h5>SDG Monitor</h5>
              <p class="text-muted">Tracking progress towards the Sustainable Development Goals.</p>
          </div>
          <div class="col-md-4">
              <h5>Quick Links</h5>
              <ul class="list-unstyled">
                  <li><a href="{{ url('/about') }}" class="text-decoration-none">About</a></li>
                  <li><a href="{{ url('/contact') }}" class="text-decoration-none">Contact</a></li>
                  <li><a href="{{ url('/faq') }}" class="text-decoration-none">FAQ</a></li>
                  <li><a href="{{ url('/privacy') }}" class="text-decoration-none">Privacy Policy</a></li>
              </ul>
          </div>
          <div class="col-md-4">
              <h5>Connect With Us</h5>
              <div class="social-icons">
                  <a href="#" class="me-2 text-decoration-none"><i class="fab fa-facebook fa-lg"></i></a>
                  <a href="#" class="me-2 text-decoration-none"><i class="fab fa-twitter fa-lg"></i></a>
                  <a href="#" class="me-2 text-decoration-none"><i
                          class="fab fa-instagram fa-lg"></i></a>
                  <a href="#" class="me-2 text-decoration-none"><i class="fab fa-linkedin fa-lg"></i></a>
                  <a href="#" class="me-2 text-decoration-none"><i class="fab fa-youtube fa-lg"></i></a>
              </div>
          </div>
      </div>
      <hr>
      <div class="d-flex justify-content-between align-items-center">
          <p class="mb-0 text-muted">&copy; {{ date('Y') }} SDG Monitor. All rights reserved.</p>
          <div>
              <button class="btn btn-sm btn-outline-secondary" id="back-to-top">
                  <i class="fas fa-arrow-up"></i> Back to top
              </button>
          </div>
      </div>
  </div>
</footer>