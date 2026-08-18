"""
Categorization ontology and method descriptions based on the complete fsspec base specification.

This module maps all methods implemented in `fsspec.spec.AbstractFileSystem`,
`fsspec.asyn.AsyncFileSystem`, and `fsspec.core` into 8 standard functional domains.
"""

from typing import Dict, List, Optional, Set

# ==============================================================================
# 8 STANDARD FUNCTIONAL CATEGORIES IN FSSPEC BASE SPEC
# ==============================================================================

CATEGORY_STREAM_IO = "Stream Reading & Writing"
CATEGORY_METADATA = "Metadata & Existence Checks"
CATEGORY_TRAVERSAL = "Directory Listing & Traversal"
CATEGORY_MUTATION = "File & Directory Mutation"
CATEGORY_TRANSFER = "Bulk Data Transfer"
CATEGORY_TOPOLOGY = "Path Arithmetic & Topologies"
CATEGORY_PROTOCOL_LIFECYCLE = "Protocol Resolution & Driver Lifecycle"
CATEGORY_WRAPPERS = "Driver Instances & Wrapper Bridges"

FSSPEC_CATEGORIES: List[str] = [
    CATEGORY_STREAM_IO,
    CATEGORY_METADATA,
    CATEGORY_TRAVERSAL,
    CATEGORY_MUTATION,
    CATEGORY_TRANSFER,
    CATEGORY_TOPOLOGY,
    CATEGORY_PROTOCOL_LIFECYCLE,
    CATEGORY_WRAPPERS,
]

# ==============================================================================
# COMPLETE FSSPEC BASE SPECIFICATION METHODS MAPPING
# ==============================================================================

FSSPEC_BASE_SPEC_METHODS: Dict[str, Dict[str, str]] = {
    # --------------------------------------------------------------------------
    # 1. Stream Reading & Writing (File I/O)
    # --------------------------------------------------------------------------
    "open": {
        "category": CATEGORY_STREAM_IO,
        "description": "Return a file-like object from the filesystem (`fs.open(path, mode)`)",
    },
    "_open": {
        "category": CATEGORY_STREAM_IO,
        "description": "Low-level implementation returning raw bytes-mode stream handle",
    },
    "open_files": {
        "category": CATEGORY_STREAM_IO,
        "description": "Batch context manager opening multiple matching file stream handles simultaneously",
    },
    "open_local": {
        "category": CATEGORY_STREAM_IO,
        "description": "Open remote path by caching to temporary local disk and returning local path string",
    },
    "open_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Open individual file handle inside protocol catalog or dataset interface",
    },
    "OpenFile": {
        "category": CATEGORY_STREAM_IO,
        "description": "Low-level context-managed open file stream handle object wrapper",
    },
    "open_parquet_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Parquet-specific byte open call supporting column group section precaching (`parts`)",
    },
    "read_block": {
        "category": CATEGORY_STREAM_IO,
        "description": "Read a fixed-size byte block range from file stream without reading entire file",
    },
    "read_bytes": {
        "category": CATEGORY_STREAM_IO,
        "description": "Alias of cat_file; get the content of a file directly as bytes",
    },
    "read_text": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the contents of the file directly decoded as a string",
    },
    "write_bytes": {
        "category": CATEGORY_STREAM_IO,
        "description": "Alias of pipe_file; write raw bytes directly to target file",
    },
    "write_text": {
        "category": CATEGORY_STREAM_IO,
        "description": "Write text string encoded directly to the given file",
    },
    "pipe": {
        "category": CATEGORY_STREAM_IO,
        "description": "Put value (bytes) into one or more paths (`fs.pipe(path, value)`)",
    },
    "pipe_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Set the byte content of a given single file",
    },
    "_pipe": {
        "category": CATEGORY_STREAM_IO,
        "description": "Asynchronous/low-level implementation piping bytes into paths",
    },
    "_pipe_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Asynchronous/low-level implementation piping bytes to a single file",
    },
    "head": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the first `size` bytes from a file header",
    },
    "tail": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the last `size` bytes from a file end",
    },
    "cat": {
        "category": CATEGORY_STREAM_IO,
        "description": "Fetch (potentially multiple) paths' byte contents as a dictionary",
    },
    "cat_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the complete byte content of a single file",
    },
    "cat_ranges": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the contents of multiple specific byte ranges from one or more files",
    },
    "_cat": {
        "category": CATEGORY_STREAM_IO,
        "description": "Asynchronous batch cat byte read across multiple keys",
    },
    "_cat_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Asynchronous/low-level direct byte range cat read of individual storage key",
    },
    "_cat_ranges": {
        "category": CATEGORY_STREAM_IO,
        "description": "Asynchronous multi-range byte chunk fetch from storage driver",
    },
    "get_mapper": {
        "category": CATEGORY_STREAM_IO,
        "description": "Create a mutable mapping (key/value dict-like) store based on this filesystem",
    },
    "open_input_stream": {
        "category": CATEGORY_STREAM_IO,
        "description": "Opening readable input byte stream from storage driver (PyArrow bridge)",
    },
    "open_input_file": {
        "category": CATEGORY_STREAM_IO,
        "description": "Opening input file handle for random-access byte read",
    },
    "open_output_stream": {
        "category": CATEGORY_STREAM_IO,
        "description": "Opening output stream handle for sequential writing",
    },
    "readinto": {
        "category": CATEGORY_STREAM_IO,
        "description": "Mirrors builtin file's readinto method; reads bytes into a pre-allocated writable buffer",
    },
    "readinto1": {
        "category": CATEGORY_STREAM_IO,
        "description": "Mirrors io.BufferedIOBase.readinto1; read up to len(b) bytes into buffer using at most one underlying read",
    },
    "read": {
        "category": CATEGORY_STREAM_IO,
        "description": "Read bytes from cache/stream, fetching chunks as necessary",
    },
    "readline": {
        "category": CATEGORY_STREAM_IO,
        "description": "Read until and including the first occurrence of newline character",
    },
    "readlines": {
        "category": CATEGORY_STREAM_IO,
        "description": "Return all lines split by the newline character, including the newline",
    },
    "readuntil": {
        "category": CATEGORY_STREAM_IO,
        "description": "Return data between current position and first occurrence of delimiter character",
    },
    "seek": {
        "category": CATEGORY_STREAM_IO,
        "description": "Set current file location offset in stream",
    },
    "tell": {
        "category": CATEGORY_STREAM_IO,
        "description": "Return current file location offset in stream",
    },
    "flush": {
        "category": CATEGORY_STREAM_IO,
        "description": "Write buffered data to backend store",
    },
    "close": {
        "category": CATEGORY_STREAM_IO,
        "description": "Close file stream handle and release buffer resources",
    },
    "readable": {
        "category": CATEGORY_STREAM_IO,
        "description": "Whether file stream handle is opened for reading",
    },
    "writable": {
        "category": CATEGORY_STREAM_IO,
        "description": "Whether file stream handle is opened for writing",
    },
    "seekable": {
        "category": CATEGORY_STREAM_IO,
        "description": "Whether file stream supports random-access seeking (only in read mode)",
    },
    "commit": {
        "category": CATEGORY_STREAM_IO,
        "description": "Move from temporary file buffer to final destination path",
    },
    "discard": {
        "category": CATEGORY_STREAM_IO,
        "description": "Throw away temporary file buffer without committing",
    },
    "write": {
        "category": CATEGORY_STREAM_IO,
        "description": "Write data bytes or string to file buffer",
    },
    "writelines": {
        "category": CATEGORY_STREAM_IO,
        "description": "Write a list of line strings/bytes to file buffer",
    },
    "truncate": {
        "category": CATEGORY_STREAM_IO,
        "description": "Truncate file stream to specified size",
    },
    "_fetch_range": {
        "category": CATEGORY_STREAM_IO,
        "description": "Get the specified set of bytes from remote store",
    },
    "_initiate_upload": {
        "category": CATEGORY_STREAM_IO,
        "description": "Create remote multipart file upload session",
    },
    "_upload_chunk": {
        "category": CATEGORY_STREAM_IO,
        "description": "Write one part of a multi-block file upload",
    },

    # --------------------------------------------------------------------------
    # 2. Metadata & Existence Checks
    # --------------------------------------------------------------------------
    "exists": {
        "category": CATEGORY_METADATA,
        "description": "Checking existence of a file or directory node on local or remote filesystem",
    },
    "lexists": {
        "category": CATEGORY_METADATA,
        "description": "Check if file or symlink exists at path without traversing link target",
    },
    "_exists": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous/internal existence check for storage key",
    },
    "info": {
        "category": CATEGORY_METADATA,
        "description": "Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`)",
    },
    "_info": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous/low-level metadata dictionary retrieval",
    },
    "stat": {
        "category": CATEGORY_METADATA,
        "description": "Alias of `info`; return status and metadata of file or directory",
    },
    "isdir": {
        "category": CATEGORY_METADATA,
        "description": "Verify whether a path points to an abstract directory container node",
    },
    "_isdir": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous directory container node check",
    },
    "isfile": {
        "category": CATEGORY_METADATA,
        "description": "Verify whether a target path resolves to a leaf file node (not a directory)",
    },
    "_isfile": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous leaf file node check",
    },
    "size": {
        "category": CATEGORY_METADATA,
        "description": "Return size in bytes of a target file",
    },
    "sizes": {
        "category": CATEGORY_METADATA,
        "description": "Return list of byte sizes for each file in a given list of paths",
    },
    "_size": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous file size lookup",
    },
    "_sizes": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous batch file size lookup across multiple keys",
    },
    "du": {
        "category": CATEGORY_METADATA,
        "description": "Calculate cumulative disk byte space consumed across a directory tree subtree",
    },
    "disk_usage": {
        "category": CATEGORY_METADATA,
        "description": "Alias of `du`; return total disk space used within directory tree",
    },
    "_du": {
        "category": CATEGORY_METADATA,
        "description": "Asynchronous disk space aggregation across directory tree",
    },
    "checksum": {
        "category": CATEGORY_METADATA,
        "description": "Unique hash/version value for current contents of file (ETag, CRC32, MD5)",
    },
    "ukey": {
        "category": CATEGORY_METADATA,
        "description": "Unique version hash or entity tag (`ETag`) for cache invalidation",
    },
    "created": {
        "category": CATEGORY_METADATA,
        "description": "Return the creation timestamp of a file as a datetime object",
    },
    "modified": {
        "category": CATEGORY_METADATA,
        "description": "Return the last-modified timestamp of a file as a datetime object",
    },
    "sign": {
        "category": CATEGORY_METADATA,
        "description": "Create a signed URL representing temporary authorized access to target path",
    },
    "_isfilestore": {
        "category": CATEGORY_METADATA,
        "description": "Boolean flag indicating whether filesystem driver represents a traditional POSIX file store",
    },
    "get_file_info": {
        "category": CATEGORY_METADATA,
        "description": "Extracting structured Arrow / PyArrow file metadata info from underlying filesystem handle",
    },

    # --------------------------------------------------------------------------
    # 3. Directory Listing & Traversal / Expansion
    # --------------------------------------------------------------------------
    "ls": {
        "category": CATEGORY_TRAVERSAL,
        "description": "List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts)",
    },
    "_ls": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Asynchronous directory listing implementation",
    },
    "listdir": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Alias of `ls`; list raw names inside target directory node",
    },
    "_ls_from_cache": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Check in-memory cache for existing directory listing",
    },
    "glob": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees",
    },
    "_glob": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Asynchronous wildcard glob matching implementation",
    },
    "find": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Recursively find all file paths inside a directory subtree matching optional criteria",
    },
    "_find": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Asynchronous low-level recursive file discovery yielding all nested keys",
    },
    "walk": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Pythonic recursive generator yielding `(root, dirs, files)` tuples across directory tree",
    },
    "_walk": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Asynchronous generator walking directory tree",
    },
    "tree": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Return a tree-like nested dictionary structure of filesystem hierarchy from root",
    },
    "expand_path": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Turn one or more glob patterns or directories into a list of all matching concrete paths",
    },
    "_expand_path": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Asynchronous path expansion implementation",
    },
    "expand_paths_if_needed": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Expanding wildcard glob strings into explicit path lists if glob syntax present",
    },
    "_expand_paths": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Internal fsspec core path expansion helper",
    },
    "FileSelector": {
        "category": CATEGORY_TRAVERSAL,
        "description": "Creating recursive file selector specification object for batch selection",
    },

    # --------------------------------------------------------------------------
    # 4. File & Directory Mutation (Creation, Move, Copy, Deletion)
    # --------------------------------------------------------------------------
    "mkdir": {
        "category": CATEGORY_MUTATION,
        "description": "Create single directory container node at path (`create_parents=False`)",
    },
    "_mkdir": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous single directory creation implementation",
    },
    "makedirs": {
        "category": CATEGORY_MUTATION,
        "description": "Recursively create directory tree hierarchy (`exist_ok=True`)",
    },
    "_makedirs": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous recursive directory hierarchy creation",
    },
    "makedir": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `mkdir`; create directory entry at path",
    },
    "mkdirs": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `makedirs`; create directory tree hierarchies",
    },
    "touch": {
        "category": CATEGORY_MUTATION,
        "description": "Create empty 0-byte file, or update timestamp if file already exists",
    },
    "rm": {
        "category": CATEGORY_MUTATION,
        "description": "Delete files or directory trees (`recursive=True/False`)",
    },
    "_rm": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous/low-level implementation deleting remote object key or prefix",
    },
    "rm_file": {
        "category": CATEGORY_MUTATION,
        "description": "Delete a single leaf file node from storage driver",
    },
    "_rm_file": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous single file deletion implementation",
    },
    "rmdir": {
        "category": CATEGORY_MUTATION,
        "description": "Remove an empty directory container node",
    },
    "delete": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `rm`; delete files or directories",
    },
    "delete_dir": {
        "category": CATEGORY_MUTATION,
        "description": "Recursively remove directory and all contained sub-keys",
    },
    "delete_file": {
        "category": CATEGORY_MUTATION,
        "description": "Deleting single file node from storage driver",
    },
    "remove": {
        "category": CATEGORY_MUTATION,
        "description": "Deleting file or folder node from underlying filesystem",
    },
    "copy": {
        "category": CATEGORY_MUTATION,
        "description": "Copy file(s) within two locations on the filesystem without downloading to local disk",
    },
    "_copy": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous intra-filesystem copy implementation",
    },
    "cp": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `copy`; copy files within storage system",
    },
    "cp_file": {
        "category": CATEGORY_MUTATION,
        "description": "Copy a single remote file from source key to destination key",
    },
    "_cp_file": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous single remote file copy",
    },
    "copy_files": {
        "category": CATEGORY_MUTATION,
        "description": "Batch copying multiple file paths within or across filesystem instances",
    },
    "move": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `mv`; move file(s) from one location to another",
    },
    "mv": {
        "category": CATEGORY_MUTATION,
        "description": "Move/rename file(s) from source path to destination path",
    },
    "_mv_file": {
        "category": CATEGORY_MUTATION,
        "description": "Asynchronous single file move/rename operation",
    },
    "rename": {
        "category": CATEGORY_MUTATION,
        "description": "Alias of `mv`; rename or move an object path within filesystem storage",
    },
    "create_dir": {
        "category": CATEGORY_MUTATION,
        "description": "Creating single directory container node inside underlying file storage",
    },

    # --------------------------------------------------------------------------
    # 5. Bulk Data Transfer (Upload / Download)
    # --------------------------------------------------------------------------
    "get": {
        "category": CATEGORY_TRANSFER,
        "description": "Bulk batch downloading of remote cloud or distributed files to local directory disk",
    },
    "_get": {
        "category": CATEGORY_TRANSFER,
        "description": "Asynchronous bulk batch download implementation",
    },
    "get_file": {
        "category": CATEGORY_TRANSFER,
        "description": "Download a single remote file to local target filename path",
    },
    "_get_file": {
        "category": CATEGORY_TRANSFER,
        "description": "Asynchronous single file download implementation",
    },
    "download": {
        "category": CATEGORY_TRANSFER,
        "description": "Alias of `get`; copy remote file(s) to local storage",
    },
    "put": {
        "category": CATEGORY_TRANSFER,
        "description": "Bulk batch uploading of local file(s) or directories up to remote filesystem target",
    },
    "_put": {
        "category": CATEGORY_TRANSFER,
        "description": "Asynchronous bulk batch upload implementation",
    },
    "put_file": {
        "category": CATEGORY_TRANSFER,
        "description": "Upload a single local file to remote target path",
    },
    "_put_file": {
        "category": CATEGORY_TRANSFER,
        "description": "Asynchronous single file upload implementation",
    },
    "upload": {
        "category": CATEGORY_TRANSFER,
        "description": "Alias of `put`; copy local file(s) to remote storage",
    },

    # --------------------------------------------------------------------------
    # 6. Path Arithmetic & Topologies
    # --------------------------------------------------------------------------
    "_parent": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Internal parent directory lookup helper extracting parent prefix",
    },
    "parent": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Locating immediate parent directory string of current path",
    },
    "join": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Cross-platform abstract POSIX path joining without OS separator assumptions",
    },
    "split": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Splitting abstract path into `(head, tail)` tuple pair",
    },
    "parts": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Splitting path string into ordered component segments tuple",
    },
    "relparts": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Deconstructing absolute path into tuple of relative path segment strings",
    },
    "relpath": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Calculating relative path string from a reference parent or root directory",
    },
    "normpath": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Normalizing redundant dot/double-dot and slash segments in paths",
    },
    "abspath": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Resolving abstract relative path to fully qualified URI path from working directory",
    },
    "getcwd": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Querying current working directory path of abstract filesystem instance",
    },
    "chdir": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Changing current working directory context of filesystem wrapper",
    },
    "isin": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Verifying whether a child path is contained within a given parent tree root",
    },
    "isin_or_eq": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Checking if path matches or falls within expected tree prefix",
    },
    "commonpath": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Find longest common sub-path prefix across multiple paths",
    },
    "as_posix": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Format path with standardized POSIX forward slash separators",
    },
    "make_path_posix": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Converting native platform separator path to standardized POSIX forward-slash path",
    },
    "stringify_path": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Coercing pathlib.Path or abstract path objects to normalized string path representation",
    },
    "concat_path": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Joining base directory prefix with relative child object key or filename",
    },
    "init_path": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Initializing root filesystem mount point path inside model or data wrapper",
    },
    "version_path": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Resolving version-tagged object store path for immutable storage backends",
    },
    "dirname": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Extracting parent directory path from abstract path string",
    },
    "name": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Extracting simple file basename string from abstract path",
    },
    "isabs": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Checking if abstract path is formatted as an absolute path",
    },
    "has_magic": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Check whether path string contains wildcard magic characters (`*`, `?`, `[]`)",
    },
    "resolve_path": {
        "category": CATEGORY_TOPOLOGY,
        "description": "Resolving symlinks or relative references in remote path",
    },

    # --------------------------------------------------------------------------
    # 7. Protocol Resolution & Driver Lifecycle
    # --------------------------------------------------------------------------
    "url_to_fs": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple",
    },
    "filesystem": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Instantiating filesystem driver class by protocol string (e.g. `fsspec.filesystem('s3')`)",
    },
    "get_filesystem_class": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Locate and return the filesystem driver class registered for a given protocol",
    },
    "get_fs_token_paths": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization",
    },
    "split_protocol": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Splitting raw string URL into `(protocol, path)` component pair",
    },
    "strip_protocol": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Remove scheme prefix from URI path string",
    },
    "_strip_protocol": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Turn path from fully-qualified URI to file-system-specific relative key",
    },
    "unstrip_protocol": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Format filesystem-specific key to generic fully-qualified URI including protocol",
    },
    "_unstrip_protocol": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Internal fsspec core helper re-attaching scheme protocol prefix",
    },
    "from_os_path": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Converting native OS filesystem path to abstract protocol URI path representation",
    },
    "_get_kwargs_from_urls": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Extract parameters and query kwargs encoded within URI path strings",
    },
    "to_dict": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "JSON-serializable dictionary representation of this filesystem instance configuration",
    },
    "from_dict": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Recreate a filesystem instance from dictionary representation",
    },
    "to_json": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "JSON string representation of this filesystem instance",
    },
    "from_json": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Recreate a filesystem instance from JSON string representation",
    },
    "__dask_tokenize__": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Dask deterministic tokenization hook for filesystem instance serialization",
    },
    "tokenize": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Generating deterministic token hash of filesystem configuration and URL paths",
    },
    "available_protocols": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "List all registered filesystem protocol schemes currently installed",
    },
    "available_compressions": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "List all registered compression and decompression codec handlers",
    },
    "infer_compression": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Detect compression format (`gzip`, `bz2`, `zip`, `zstd`) from file extension suffix",
    },
    "get_compression": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Retrieve compression wrapper and mode for a given compression name",
    },
    "register_implementation": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Register custom filesystem driver implementation under a protocol scheme",
    },
    "clear_instance_cache": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Clear the global cache of singleton filesystem instances",
    },
    "current": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Return the most recently instantiated filesystem driver instance",
    },
    "start_transaction": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Begin write transaction for deferring and batching file commits",
    },
    "end_transaction": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Finish and commit write transaction across filesystem",
    },
    "invalidate_cache": {
        "category": CATEGORY_PROTOCOL_LIFECYCLE,
        "description": "Discard any cached directory and file metadata information",
    },

    # --------------------------------------------------------------------------
    # 8. Driver Instances & Wrapper Bridges
    # --------------------------------------------------------------------------
    "_get_pyarrow_filesystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Construct a PyArrow-compatible filesystem instance wrapping this fsspec driver",
    },
    "ArrowFSWrapper": {
        "category": CATEGORY_WRAPPERS,
        "description": "Instantiating PyArrow filesystem interface wrapper around fsspec driver",
    },
    "DirFileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Wrapping directory root so relative paths operate within a sub-tree sandbox",
    },
    "LocalFileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Instantiating explicit local host disk filesystem driver (`file://`)",
    },
    "GCSFileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Instantiating Google Cloud Storage (`gs://`) filesystem driver",
    },
    "S3FileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Instantiating Amazon S3 (`s3://`) filesystem backend driver",
    },
    "AzureBlobFileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "Instantiating Azure Blob / ADLS (`abfs://`) filesystem backend driver",
    },
    "PyFileSystem": {
        "category": CATEGORY_WRAPPERS,
        "description": "PyArrow filesystem representation wrapping abstract driver",
    },
    "FSSpecHandler": {
        "category": CATEGORY_WRAPPERS,
        "description": "PyArrow custom filesystem bridge handler wrapping fsspec driver",
    },
    "is_remote": {
        "category": CATEGORY_WRAPPERS,
        "description": "Boolean flag checking whether abstract storage driver targets cloud/remote backend",
    },
    "unwrap": {
        "category": CATEGORY_WRAPPERS,
        "description": "Unwrapping abstract wrapper object to extract underlying native filesystem instance",
    },
    "isdvc": {
        "category": CATEGORY_WRAPPERS,
        "description": "DVC custom validation call checking whether path is tracked under version control",
    },
}

# ==============================================================================
# COMPOSITE USAGE PATTERNS LOOKUP (Includes instance calls like self.fs.open)
# ==============================================================================

USAGE_PATTERNS: Dict[str, str] = {}

# Populate USAGE_PATTERNS from base spec
for method_name, meta in FSSPEC_BASE_SPEC_METHODS.items():
    USAGE_PATTERNS[method_name] = meta["description"]
    USAGE_PATTERNS[f"fs.{method_name}"] = meta["description"]
    USAGE_PATTERNS[f"self.fs.{method_name}"] = f"Instance method: {meta['description']}"
    USAGE_PATTERNS[f"fsspec.{method_name}"] = f"fsspec module: {meta['description']}"
    USAGE_PATTERNS[f"filesystem.{method_name}"] = f"Filesystem wrapper: {meta['description']}"
    USAGE_PATTERNS[f"self.filesystem.{method_name}"] = f"Instance filesystem wrapper: {meta['description']}"


# ==============================================================================
# CATEGORIZATION ENGINE
# ==============================================================================

def _extract_base_method_name(full_name: str) -> str:
    """Extract clean method name from composite call (e.g. self.fs.open -> open)."""
    return full_name.split(".")[-1].strip()


def is_fsspec_base_method(name: str) -> bool:
    """Check if a method name is part of the fsspec base specification."""
    base_name = _extract_base_method_name(name)
    return base_name in FSSPEC_BASE_SPEC_METHODS or name in FSSPEC_BASE_SPEC_METHODS


def get_method_description(name: str) -> str:
    """Return descriptive pattern for a method from fsspec base spec or fallback."""
    if name in USAGE_PATTERNS:
        return USAGE_PATTERNS[name]
    base_name = _extract_base_method_name(name)
    if base_name in FSSPEC_BASE_SPEC_METHODS:
        return FSSPEC_BASE_SPEC_METHODS[base_name]["description"]
    cat = categorize_method(name)
    return f"{cat} API method detected across storage interactions"


def get_methods_in_category(category: str) -> List[str]:
    """Return all fsspec base spec method names belonging to a category."""
    return [
        m
        for m, meta in FSSPEC_BASE_SPEC_METHODS.items()
        if meta["category"].lower() == category.lower()
    ]


def categorize_method(name: str) -> str:
    """
    Categorize any fsspec or filesystem method call into one of the 8 standard
    functional domains defined by the fsspec base specification.
    """
    base_name = _extract_base_method_name(name)

    # 1. Exact lookup in fsspec base specification
    if base_name in FSSPEC_BASE_SPEC_METHODS:
        return FSSPEC_BASE_SPEC_METHODS[base_name]["category"]
    if name in FSSPEC_BASE_SPEC_METHODS:
        return FSSPEC_BASE_SPEC_METHODS[name]["category"]

    # 2. Heuristic fallback based on method name components
    n = base_name.lower()

    if any(
        k in n
        for k in [
            "exists",
            "info",
            "isdir",
            "isfile",
            "size",
            "du",
            "stat",
            "checksum",
            "ukey",
            "version",
            "is_empty",
            "modified",
            "created",
            "sign",
        ]
    ):
        return CATEGORY_METADATA

    elif any(
        k in n
        for k in [
            "open",
            "cat",
            "read",
            "write",
            "pipe",
            "head",
            "tail",
            "stream",
            "mapper",
        ]
    ):
        return CATEGORY_STREAM_IO

    elif any(
        k in n
        for k in [
            "glob",
            "find",
            "walk",
            "ls",
            "list",
            "tree",
            "expand",
            "selector",
        ]
    ):
        return CATEGORY_TRAVERSAL

    elif any(
        k in n
        for k in [
            "mkdir",
            "make",
            "touch",
            "rm",
            "remove",
            "delete",
            "copy",
            "cp",
            "move",
            "mv",
            "rename",
        ]
    ):
        return CATEGORY_MUTATION

    elif any(k in n for k in ["get", "put", "download", "upload"]):
        return CATEGORY_TRANSFER

    elif any(
        k in n
        for k in [
            "parent",
            "join",
            "split",
            "parts",
            "relparts",
            "relpath",
            "normpath",
            "abspath",
            "getcwd",
            "chdir",
            "isin",
            "commonpath",
            "as_posix",
            "posix",
            "stringify",
            "concat",
            "dirname",
            "name",
            "isabs",
        ]
    ):
        return CATEGORY_TOPOLOGY

    elif any(
        k in n
        for k in [
            "url_to_fs",
            "filesystem",
            "token",
            "protocol",
            "strip",
            "unstrip",
            "from_os",
            "dict",
            "json",
            "transaction",
            "cache",
            "compression",
            "register",
        ]
    ):
        return CATEGORY_PROTOCOL_LIFECYCLE

    else:
        return CATEGORY_WRAPPERS
