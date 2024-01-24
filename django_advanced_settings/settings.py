from typing import Optional, Tuple, Union, Literal, Any, Pattern, Callable, List, cast
from pydantic_settings import BaseSettings, SettingsConfigDict
from django.conf import global_settings
from pydantic import (
    DirectoryPath,
    EmailStr,
    AnyHttpUrl,
    IPvAnyAddress,
    FilePath,
    Field,
)

from django_advanced_settings.schemas import (
    DatabaseSchema,
    StoragesSchema,
    SameSiteFlag,
    CachesSchema,
    MessageStorageDotPath,
    ReferrerPolicy,
    CrossOrigin,
    SecurityCheck,
    XFrameOptions,
    DottedString,
)


class DjangoGlobalSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DJANGO_", env_file=".env", extra="ignore"
    )

    DEBUG: bool = global_settings.DEBUG
    DEBUG_PROPAGATE_EXCEPTIONS: bool = global_settings.DEBUG_PROPAGATE_EXCEPTIONS
    ADMINS: List[Tuple[EmailStr, str]] = global_settings.ADMINS
    INTERNAL_IPS: List[
        str
    ] = global_settings.INTERNAL_IPS  # TODO: write the correct type
    ALLOWED_HOSTS: List[
        str
    ] = global_settings.ALLOWED_HOSTS  # TODO: write the correct type
    TIME_ZONE: str = global_settings.TIME_ZONE
    USE_TZ: bool = global_settings.USE_TZ
    LANGUAGES: List[Tuple[str, str]] = global_settings.LANGUAGES
    LANGUAGES_BIDI: List[str] = global_settings.LANGUAGES_BIDI
    USE_I18N: bool = global_settings.USE_I18N
    LOCALE_PATHS: List[DirectoryPath] = cast(
        List[DirectoryPath], global_settings.LOCALE_PATHS
    )
    LANGUAGE_COOKIE_NAME: str = global_settings.LANGUAGE_COOKIE_NAME
    LANGUAGE_COOKIE_AGE: Optional[int] = global_settings.LANGUAGE_COOKIE_AGE
    LANGUAGE_COOKIE_DOMAIN: Optional[str] = global_settings.LANGUAGE_COOKIE_DOMAIN
    LANGUAGE_COOKIE_PATH: str = global_settings.LANGUAGE_COOKIE_PATH
    LANGUAGE_COOKIE_SECURE: bool = global_settings.LANGUAGE_COOKIE_SECURE
    LANGUAGE_COOKIE_HTTPONLY: bool = global_settings.LANGUAGE_COOKIE_HTTPONLY
    MANAGERS: List[Tuple[str, str]] = global_settings.MANAGERS
    DEFAULT_CHARSET: str = global_settings.DEFAULT_CHARSET
    SERVER_EMAIL: Union[
        EmailStr, Literal["root@localhost"]
    ] = global_settings.SERVER_EMAIL
    DATABASES: dict[str, DatabaseSchema] = cast(
        dict[str, DatabaseSchema], global_settings.DATABASES
    )
    DATABASE_ROUTERS: Optional[List[DottedString]] = cast(
        Optional[List[DottedString]], global_settings.DATABASE_ROUTERS
    )
    EMAIL_BACKEND: DottedString = global_settings.EMAIL_BACKEND
    EMAIL_HOST: Union[AnyHttpUrl, IPvAnyAddress, Literal["localhost"]] = cast(
        Union[AnyHttpUrl, IPvAnyAddress, Literal["localhost"]],
        global_settings.EMAIL_HOST,
    )
    EMAIL_PORT: int = global_settings.EMAIL_PORT
    EMAIL_USE_LOCALTIME: bool = global_settings.EMAIL_USE_LOCALTIME
    EMAIL_HOST_USER: str = global_settings.EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD: str = global_settings.EMAIL_HOST_PASSWORD
    EMAIL_USE_TLS: bool = global_settings.EMAIL_USE_TLS
    EMAIL_USE_SSL: bool = global_settings.EMAIL_USE_SSL
    EMAIL_SSL_CERTFILE: Optional[FilePath] = cast(
        Optional[FilePath], global_settings.EMAIL_SSL_CERTFILE
    )
    EMAIL_SSL_KEYFILE: Optional[FilePath] = cast(
        Optional[FilePath], global_settings.EMAIL_SSL_KEYFILE
    )
    EMAIL_TIMEOUT: Optional[int] = global_settings.EMAIL_TIMEOUT
    INSTALLED_APPS: List[str] = global_settings.INSTALLED_APPS
    TEMPLATES: List = global_settings.TEMPLATES  # TODO: write the correct type
    FORM_RENDERER: DottedString = global_settings.FORM_RENDERER
    DEFAULT_FROM_EMAIL: Union[
        EmailStr, Literal["webmaster@localhost"]
    ] = global_settings.DEFAULT_FROM_EMAIL

    EMAIL_SUBJECT_PREFIX: str = global_settings.EMAIL_SUBJECT_PREFIX
    APPEND_SLASH: bool = global_settings.APPEND_SLASH
    PREPEND_WWW: bool = global_settings.PREPEND_WWW
    FORCE_SCRIPT_NAME: Any = global_settings.FORCE_SCRIPT_NAME
    DISALLOWED_USER_AGENTS: List[Pattern] = global_settings.DISALLOWED_USER_AGENTS
    ABSOLUTE_URL_OVERRIDES: dict[str, Callable] = global_settings.ABSOLUTE_URL_OVERRIDES
    IGNORABLE_404_URLS: List[Pattern] = global_settings.IGNORABLE_404_URLS
    SECRET_KEY: str = cast(str, global_settings.SECRET_KEY)
    SECRET_KEY_FALLBACKS: List[str] = cast(
        List[str], global_settings.SECRET_KEY_FALLBACKS
    )
    DEFAULT_FILE_STORAGE: DottedString = global_settings.DEFAULT_FILE_STORAGE
    STORAGES: dict[str, StoragesSchema] = cast(
        dict[str, StoragesSchema], global_settings.STORAGES
    )  # New in Django 4.2.
    MEDIA_ROOT: Union[DirectoryPath, Literal[""]] = cast(
        Union[DirectoryPath, Literal[""]], global_settings.MEDIA_ROOT
    )
    MEDIA_URL: Union[AnyHttpUrl, Literal[""]] = cast(
        Union[AnyHttpUrl, Literal[""]], global_settings.MEDIA_URL
    )
    STATIC_ROOT: Optional[DirectoryPath] = cast(
        Optional[DirectoryPath], global_settings.STATIC_ROOT
    )
    STATIC_URL: Union[str, None] = global_settings.STATIC_URL
    FILE_UPLOAD_HANDLERS: List[DottedString] = global_settings.FILE_UPLOAD_HANDLERS
    FILE_UPLOAD_MAX_MEMORY_SIZE: int = global_settings.FILE_UPLOAD_MAX_MEMORY_SIZE
    DATA_UPLOAD_MAX_MEMORY_SIZE: int = global_settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    DATA_UPLOAD_MAX_NUMBER_FIELDS: int = global_settings.DATA_UPLOAD_MAX_NUMBER_FIELDS
    DATA_UPLOAD_MAX_NUMBER_FILES: int = global_settings.DATA_UPLOAD_MAX_NUMBER_FILES
    FILE_UPLOAD_TEMP_DIR: Optional[DirectoryPath] = cast(
        Optional[DirectoryPath], global_settings.FILE_UPLOAD_TEMP_DIR
    )
    FILE_UPLOAD_PERMISSIONS: int = global_settings.FILE_UPLOAD_PERMISSIONS
    FILE_UPLOAD_DIRECTORY_PERMISSIONS: Union[
        int, None
    ] = global_settings.FILE_UPLOAD_DIRECTORY_PERMISSIONS
    FORMAT_MODULE_PATH: Optional[DottedString] = global_settings.FORMAT_MODULE_PATH
    DATE_FORMAT: str = global_settings.DATE_FORMAT
    DATETIME_FORMAT: str = global_settings.DATETIME_FORMAT
    TIME_FORMAT: str = global_settings.TIME_FORMAT
    YEAR_MONTH_FORMAT: str = global_settings.YEAR_MONTH_FORMAT
    MONTH_DAY_FORMAT: str = global_settings.MONTH_DAY_FORMAT
    SHORT_DATE_FORMAT: str = global_settings.SHORT_DATE_FORMAT
    SHORT_DATETIME_FORMAT: str = global_settings.SHORT_DATETIME_FORMAT
    DATE_INPUT_FORMATS: List[str] = global_settings.DATE_INPUT_FORMATS
    TIME_INPUT_FORMATS: List[str] = global_settings.TIME_INPUT_FORMATS
    DATETIME_INPUT_FORMATS: List[str] = global_settings.DATETIME_INPUT_FORMATS
    FIRST_DAY_OF_WEEK: int = Field(global_settings.FIRST_DAY_OF_WEEK, ge=0, le=6)
    DECIMAL_SEPARATOR: str = global_settings.DECIMAL_SEPARATOR
    USE_THOUSAND_SEPARATOR: bool = global_settings.USE_THOUSAND_SEPARATOR
    NUMBER_GROUPING: int = global_settings.NUMBER_GROUPING
    THOUSAND_SEPARATOR: str = global_settings.THOUSAND_SEPARATOR
    DEFAULT_TABLESPACE: str = global_settings.DEFAULT_TABLESPACE
    DEFAULT_INDEX_TABLESPACE: str = global_settings.DEFAULT_INDEX_TABLESPACE
    DEFAULT_AUTO_FIELD: DottedString = global_settings.DEFAULT_AUTO_FIELD
    X_FRAME_OPTIONS: XFrameOptions = cast(
        XFrameOptions, global_settings.X_FRAME_OPTIONS
    )
    USE_X_FORWARDED_HOST: bool = global_settings.USE_X_FORWARDED_HOST
    USE_X_FORWARDED_PORT: bool = global_settings.USE_X_FORWARDED_PORT
    WSGI_APPLICATION: Optional[DottedString] = global_settings.WSGI_APPLICATION

    SECURE_PROXY_SSL_HEADER: Union[
        Tuple, None
    ] = global_settings.SECURE_PROXY_SSL_HEADER
    MIDDLEWARE: List[DottedString] = global_settings.MIDDLEWARE
    SESSION_CACHE_ALIAS: str = global_settings.SESSION_CACHE_ALIAS
    SESSION_COOKIE_NAME: str = global_settings.SESSION_COOKIE_NAME
    SESSION_COOKIE_AGE: int = global_settings.SESSION_COOKIE_AGE
    SESSION_COOKIE_DOMAIN: Optional[str] = global_settings.SESSION_COOKIE_DOMAIN
    SESSION_COOKIE_SECURE: bool = global_settings.SESSION_COOKIE_SECURE
    SESSION_COOKIE_PATH: str = global_settings.SESSION_COOKIE_PATH
    SESSION_COOKIE_HTTPONLY: bool = global_settings.SESSION_COOKIE_HTTPONLY
    SESSION_COOKIE_SAMESITE: SameSiteFlag = global_settings.SESSION_COOKIE_SAMESITE
    SESSION_SAVE_EVERY_REQUEST: bool = global_settings.SESSION_SAVE_EVERY_REQUEST
    SESSION_EXPIRE_AT_BROWSER_CLOSE: bool = (
        global_settings.SESSION_EXPIRE_AT_BROWSER_CLOSE
    )
    SESSION_ENGINE: DottedString = global_settings.SESSION_ENGINE
    SESSION_FILE_PATH: Optional[DirectoryPath] = cast(
        Optional[DirectoryPath], global_settings.SESSION_FILE_PATH
    )
    SESSION_SERIALIZER: DottedString = global_settings.SESSION_SERIALIZER
    CACHES: dict[str, CachesSchema] = cast(
        dict[str, CachesSchema], global_settings.CACHES
    )
    CACHE_MIDDLEWARE_KEY_PREFIX: str = global_settings.CACHE_MIDDLEWARE_KEY_PREFIX
    CACHE_MIDDLEWARE_SECONDS: int = global_settings.CACHE_MIDDLEWARE_SECONDS
    CACHE_MIDDLEWARE_ALIAS: str = global_settings.CACHE_MIDDLEWARE_ALIAS
    AUTH_USER_MODEL: str = global_settings.AUTH_USER_MODEL
    AUTHENTICATION_BACKENDS: List[DottedString] = cast(
        List[DottedString], global_settings.AUTHENTICATION_BACKENDS
    )
    LOGIN_URL: str = global_settings.LOGIN_URL
    LOGIN_REDIRECT_URL: str = global_settings.LOGIN_REDIRECT_URL
    LOGOUT_REDIRECT_URL: Optional[str] = global_settings.LOGOUT_REDIRECT_URL
    PASSWORD_RESET_TIMEOUT: int = global_settings.PASSWORD_RESET_TIMEOUT
    PASSWORD_HASHERS: List[DottedString] = global_settings.PASSWORD_HASHERS
    AUTH_PASSWORD_VALIDATORS: List[
        dict[str, DottedString]
    ] = global_settings.AUTH_PASSWORD_VALIDATORS
    SIGNING_BACKEND: DottedString = global_settings.SIGNING_BACKEND
    CSRF_FAILURE_VIEW: DottedString = global_settings.CSRF_FAILURE_VIEW
    CSRF_COOKIE_NAME: str = global_settings.CSRF_COOKIE_NAME
    CSRF_COOKIE_AGE: int = global_settings.CSRF_COOKIE_AGE
    CSRF_COOKIE_DOMAIN: Optional[AnyHttpUrl] = cast(
        Optional[AnyHttpUrl], global_settings.CSRF_COOKIE_DOMAIN
    )
    CSRF_COOKIE_PATH: str = global_settings.CSRF_COOKIE_PATH
    CSRF_COOKIE_SECURE: bool = global_settings.CSRF_COOKIE_SECURE
    CSRF_COOKIE_HTTPONLY: bool = global_settings.CSRF_COOKIE_HTTPONLY
    CSRF_COOKIE_SAMESITE: SameSiteFlag = global_settings.CSRF_COOKIE_SAMESITE
    CSRF_HEADER_NAME: str = global_settings.CSRF_HEADER_NAME
    CSRF_TRUSTED_ORIGINS: List[str] = global_settings.CSRF_TRUSTED_ORIGINS
    CSRF_USE_SESSIONS: bool = global_settings.CSRF_USE_SESSIONS
    CSRF_COOKIE_MASKED: bool = global_settings.CSRF_COOKIE_MASKED
    MESSAGE_STORAGE: MessageStorageDotPath = cast(
        MessageStorageDotPath, global_settings.MESSAGE_STORAGE
    )
    LOGGING_CONFIG: DottedString = global_settings.LOGGING_CONFIG
    LOGGING: dict = global_settings.LOGGING
    DEFAULT_EXCEPTION_REPORTER: DottedString = (
        global_settings.DEFAULT_EXCEPTION_REPORTER
    )
    DEFAULT_EXCEPTION_REPORTER_FILTER: DottedString = (
        global_settings.DEFAULT_EXCEPTION_REPORTER_FILTER
    )
    TEST_RUNNER: DottedString = global_settings.TEST_RUNNER
    TEST_NON_SERIALIZED_APPS: List[
        DottedString
    ] = global_settings.TEST_NON_SERIALIZED_APPS
    FIXTURE_DIRS: List[DirectoryPath] = cast(
        List[DirectoryPath], global_settings.FIXTURE_DIRS
    )
    STATICFILES_DIRS: List[DirectoryPath] = cast(
        List[DirectoryPath], global_settings.STATICFILES_DIRS
    )
    STATICFILES_STORAGE: DottedString = global_settings.STATICFILES_STORAGE
    STATICFILES_FINDERS: List[DottedString] = global_settings.STATICFILES_FINDERS
    MIGRATION_MODULES: dict[str, DottedString] = global_settings.MIGRATION_MODULES
    SILENCED_SYSTEM_CHECKS: List[SecurityCheck] = cast(
        List[SecurityCheck], global_settings.SILENCED_SYSTEM_CHECKS
    )
    SECURE_CONTENT_TYPE_NOSNIFF: bool = global_settings.SECURE_CONTENT_TYPE_NOSNIFF
    SECURE_CROSS_ORIGIN_OPENER_POLICY: Optional[CrossOrigin] = cast(
        CrossOrigin, global_settings.SECURE_CROSS_ORIGIN_OPENER_POLICY
    )
    SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = (
        global_settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
    )
    SECURE_HSTS_PRELOAD: bool = global_settings.SECURE_HSTS_PRELOAD
    SECURE_HSTS_SECONDS: int = global_settings.SECURE_HSTS_SECONDS
    SECURE_REDIRECT_EXEMPT: List[str] = global_settings.SECURE_REDIRECT_EXEMPT
    SECURE_REFERRER_POLICY: ReferrerPolicy = cast(
        ReferrerPolicy, global_settings.SECURE_REFERRER_POLICY
    )
    SECURE_SSL_HOST: Optional[str] = global_settings.SECURE_SSL_HOST
    SECURE_SSL_REDIRECT: bool = global_settings.SECURE_SSL_REDIRECT


class DefaultSettings(DjangoGlobalSettings):
    DEBUG: bool = True
    ALLOWED_HOSTS: List[str] = ["*"]
    INSTALLED_APPS: List[str] = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    MIDDLEWARE: List[DottedString] = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    TEMPLATES: List = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    AUTH_PASSWORD_VALIDATORS: List[dict[str, DottedString]] = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    LANGUAGE_CODE: str = "en-us"

    TIME_ZONE: str = "UTC"

    USE_I18N: bool = True

    USE_TZ: bool = True

    STATIC_URL: Union[str, None] = "static/"

    DEFAULT_AUTO_FIELD: DottedString = "django.db.models.BigAutoField"
