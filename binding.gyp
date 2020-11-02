{
    "targets": [
        {
            "target_name": "node-simconnect",
            "sources": [ "src/addon.cc" ],
            "include_dirs": [
                "./SimConnect SDK/include",
				"<!(node -e \"require('nan')\")"
            ],
            "link_settings": {
                "libraries": [
                    "../SimConnect SDK/lib/SimConnect"
                ]
            },
            'configurations': {
                'Debug': {
                    'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': '3' # /MDd
                        }
                    }
                },
                'Release': {
                    'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': '2' # /MD
                        }
                    }
                }
            }
        }
    ]
    
	
	
}