.. currentmodule:: flask_wtf.csrf

.. _csrf:

CSRF Protection
===============

Any view using :class:`~flask_wtf.FlaskForm` to process the request is already
getting CSRF protection. If you have views that don't use ``FlaskForm`` or make
AJAX requests, use the provided CSRF extension to protect those requests as
well.

Setup
-----

To enable CSRF protection globally for a Flask app, register the
:class:`CSRFProtect` extension. ::

    from flask_wtf.csrf import CSRFProtect

    csrf = CSRFProtect(app)

Like other Flask extensions, you can apply it lazily::

    csrf = CSRFProtect()

    def create_app():
        app = Flask(__name__)
        csrf.init_app(app)

.. note::

    CSRF protection requires a secret key to securely sign the token. By default
    this will use the Flask app's ``SECRET_KEY``. If you'd like to use a
    separate token you can set ``WTF_CSRF_SECRET_KEY``.

HTML Forms
----------

When using a ``FlaskForm``, render the form's CSRF field like normal.

.. sourcecode:: html+jinja

    <form method="post">
        {{ form.csrf_token }}
    </form>

If the template doesn't use a ``FlaskForm``, render a hidden input with the
token in the form.

.. sourcecode:: html+jinja

    <form method="post">
        <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
    </form>

JavaScript Requests
-------------------

When sending an AJAX request, add the ``X-CSRFToken`` header to it.
For example, in jQuery you can configure all requests to send the token.

.. sourcecode:: html+jinja

    <script type="text/javascript">
        var csrf_token = "{{ csrf_token() }}";

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });
    </script>

In Axios you can set the header for all requests with ``axios.defaults.headers.common``.

.. sourcecode:: html+jinja

    <script type="text/javascript">
        axios.defaults.headers.common["X-CSRFToken"] = "{{ csrf_token() }}";
    </script>

Customize the error response
----------------------------

When CSRF validation fails, it will raise a :class:`CSRFError`.
By default this returns a response with the failure reason and a 400 code.
You can customize the error response using Flask's
:meth:`~flask.Flask.errorhandler`. ::

    from flask_wtf.csrf import CSRFError

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('csrf_error.html', reason=e.description), 400

Exclude views from protection
-----------------------------

We strongly suggest that you protect all your views with CSRF. But if
needed, you can exclude some views using a decorator. ::

    @app.route('/foo', methods=('GET', 'POST'))
    @csrf.exempt
    def my_handler():
        # ...
        return 'ok'

You can exclude all the views of a blueprint. ::

    csrf.exempt(account_blueprint)

You can disable CSRF protection in all views by default, by setting
``WTF_CSRF_CHECK_DEFAULT`` to ``False``, and selectively call
:meth:`~flask_wtf.csrf.CSRFProtect.protect` only when you need. This also enables you to do some
pre-processing on the requests before checking for the CSRF token. ::

    @app.before_request
    def check_csrf():
        if not is_oauth(request):
            csrf.protect()
