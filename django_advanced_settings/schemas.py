from typing import Union, Optional, Literal, Annotated, List
from pydantic import BaseModel, AnyUrl, IPvAnyAddress, StringConstraints, FilePath


DottedString = Annotated[
    str, StringConstraints(pattern=r"^([a-zA-Z_\d]+\.)+[a-zA-Z_\d]+$")
]

ReferrerPolicy = Literal[
    "no-referrer",
    "no-referrer-when-downgrade",
    "origin",
    "origin-when-cross-origin",
    "same-origin",
    "strict-origin",
    "strict-origin-when-cross-origin",
    "unsafe-url",
]

CrossOrigin = Literal["same-origin", "same-origin-allow-popups", "unsafe-none"]

SameSiteFlag = Literal["Lax", "Strict", "None", False]

MessageStorageDotPath = Literal[
    "django.contrib.messages.storage.fallback.FallbackStorage",
    "django.contrib.messages.storage.session.SessionStorage",
    "django.contrib.messages.storage.cookie.CookieStorage",
]

XFrameOptions = Literal["DENY", "SAMEORIGIN", "ALLOW-FROM origin"]

SecurityCheck = Literal[
    "security.W001",
    "security.W002",
    "security.W003",
    "security.W004",
    "security.W005",
    "security.W006",
    "security.W007",
    "security.W008",
    "security.W009",
    "security.W010",
    "security.W011",
    "security.W012",
    "security.W013",
    "security.W014",
    "security.W015",
    "security.W016",
    "security.W017",
    "security.W018",
    "security.W019",
    "security.W020",
    "security.W021",
    "security.W022",
    "security.E023",
    "security.E024",
    "security.W025",
    "security.E100",
    "security.E101",
    "security.E102",
]


class DatabaseTestSchema(BaseModel):
    CHARSET: Optional[str] = None
    COLLATION: Optional[str] = None  # MySQL-specific setting
    DEPENDENCIES: List[str] = ["default"]
    MIGRATE: bool = True
    MIRROR: Optional[str] = None
    NAME: Optional[str] = None
    SERIALIZE: bool  # Deprecated since version 4.0
    TEMPLATE: str  # PostgreSQL-specific setting
    CREATE_DB: bool  # Oracle-specific setting
    CREATE_USER: bool  # Oracle-specific setting
    USER: Optional[str] = None  # Oracle-specific setting
    PASSWORD: Optional[str] = None  # Oracle-specific setting
    ORACLE_MANAGED_FILES: bool  # Oracle-specific setting
    TBLSPACE: Optional[str]  # Oracle-specific setting
    TBLSPACE_TMP: Optional[str]  # Oracle-specific setting
    DATAFILE: Optional[str]  # Oracle-specific setting
    DATAFILE_TMP: Optional[str]  # Oracle-specific setting
    DATAFILE_MAXSIZE: str = "500M"  # Oracle-specific setting
    DATAFILE_TMP_MAXSIZE: str = "500M"  # Oracle-specific setting
    DATAFILE_SIZE: str = "50M"  # Oracle-specific setting
    DATAFILE_TMP_SIZE: str = "50M"  # Oracle-specific setting
    DATAFILE_EXTSIZE: str = "25M"  # Oracle-specific setting
    DATAFILE_TMP_EXTSIZE: str = "25M"  # Oracle-specific setting


class DatabaseSchema(BaseModel):
    ENGINE: DottedString
    NAME: Union[str, FilePath]
    USER: Optional[str] = None
    PASSWORD: Optional[str] = None
    HOST: Union[AnyUrl, IPvAnyAddress, None] = None
    PORT: Optional[str] = None
    ATOMIC_REQUESTS: bool = False
    AUTOCOMMIT: bool = True
    CONN_MAX_AGE: int = 0
    CONN_HEALTH_CHECKS: bool = False  # new in django 4.1
    OPTIONS: dict = {}
    TIME_ZONE: Optional[str] = None
    DISABLE_SERVER_SIDE_CURSORS: bool = False
    TEST: dict[str, DatabaseTestSchema] = {}


class StoragesSchema(BaseModel):
    BACKEND: DottedString
    OPTIONS: Optional[dict[str, str]] = None


class CachesSchema(BaseModel):
    BACKEND: DottedString


class PasswordValidatorSchema(BaseModel):
    NAME: DottedString
    OPTIONS: Optional[dict[str, Union[str, int]]] = None
