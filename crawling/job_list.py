FRONT_STACK_LIST = {
    "frameworks": ["react", "next.js", "vue", "nuxt.js", "angular", "svelte", "solid.js", "astro", "qwik"],
    "languages": ["typescript", "javascript"],
    "styling": ["tailwindcss", "bootstrap", "material-ui", "chakra-ui", "styled-components", "emotion", "sass", "less"],
    "state_management": ["redux", "zustand", "mobx", "recoil", "jotai", "tanstack-query", "swr"],
    "build_tools": ["webpack", "vite", "rollup", "parcel", "turbopack"],
    "code_quality": ["babel", "eslint", "prettier", "husky", "lint-staged"],
    "testing": ["jest", "cypress", "playwright", "storybook", "vitest", "react-testing-library"],
    "api": ["graphql", "apollo client", "urql", "axios", "fetch"],
    "special_features": ["pwa", "webassembly", "three.js", "d3.js", "chart.js", "framer-motion"],
    "form_handling": ["react-hook-form", "formik", "yup", "zod"],
    "i18n": ["i18next", "react-intl"],
}
BACK_STACK_LIST = {
    "node_ecosystem": ["node.js", "express", "nest.js", "koa", "fastify"],
    "java_ecosystem": ["spring", "spring boot", "java", "kotlin", "quarkus", "micronaut"],
    "python_ecosystem": ["django", "flask", "fastapi", "python", "tornado"],
    "other_frameworks": ["ruby on rails", "laravel", "php", "asp.net", "c#", "go", "gin", "echo"],
    "api_tech": ["graphql", "apollo server", "rest api", "swagger", "openapi"],
    "sql_databases": ["mysql", "postgresql", "mariadb"],
    "nosql_databases": ["mongodb", "redis", "cassandra", "dynamodb", "couchbase"],
    "messaging": ["elasticsearch", "kafka", "rabbitmq", "nats", "grpc", "protobuf"],
    "container_server": ["docker", "kubernetes", "nginx", "apache"],
    "orm": ["prisma", "typeorm", "sequelize", "sqlalchemy", "mongoose", "hibernate"],
    "testing": ["jest", "mocha", "junit", "pytest", "mockito", "supertest"]
}
IOS_STACK_LIST = {
    "languages": ["swift", "objective-c"],
    "frameworks": ["swiftui", "uikit"],
    "storage": ["coredata", "realm"],
    "networking": ["alamofire", "moya"],
    "testing": ["xctest", "quick", "nimble", "metrickit"]
}

CROSS_STACK_LIST = {
    "frameworks": ["react native", "flutter", "xamarin"],
    "testing": ["detox", "appium", "fastlane", "firebase test lab"]
}

ANDROID_STACK_LIST = {
    "languages": ["kotlin", "java"],
    "frameworks": ["android sdk", "android jetpack", "jetpack compose"],
    "storage": ["room", "realm"],
    "networking": ["retrofit", "okhttp"],
    "testing": ["espresso", "junit", "mockk", "robolectric"]
}
GAME_STACK_LIST = {
    "engines": ["unity", "unreal engine", "godot", "cryengine", "cocos2d-x", "gamemaker studio"],
    "graphics": ["blender", "maya", "3ds max", "openGL", "directX", "vulkan"],
    "audio": ["fmod", "wwise"],
    "shaders": ["hlsl", "glsl"],
    "platforms": ["steamworks", "xbox live sdk", "psn sdk"],
    "testing": ["unity test framework", "unreal automation", "gamelift"]
}
SECURITY_STACK_LIST = {
    "network_tools": ["kali linux", "wireshark", "nmap", "metasploit", "burp suite", "nessus", "openvas", "snort", "suricata"],
    "monitoring": ["osquery", "splunk", "elk stack", "nagios", "zabbix", "prometheus"],
    "pentesting": ["hashcat", "john the ripper", "sqlmap", "aircrack-ng", "metasploit framework"],
    "iam": ["cloudflare", "okta", "auth0", "mfa", "sso", "saml", "oauth2", "keycloak"],
    "encryption": ["veracrypt", "keepass", "gpg", "tor", "vpn", "vault"],
    "container_security": ["aqua", "twistlock", "snyk"],
    "testing": ["owasp zap", "acunetix", "netsparker", "fortify", "checkmarx"]
}

CLOUD_STACK_LIST = {
    "providers": ["aws", "gcp", "azure", "digitalocean", "oracle cloud", "naver cloud", "kakao cloud"],
    "container_orchestration": ["docker", "kubernetes", "helm", "istio", "nginx", "rancher"],
    "iac": ["terraform", "cloudformation", "pulumi", "ansible", "chef", "puppet", "cdk"],
    "ci_cd": ["jenkins", "github actions", "gitlab ci", "circleci", "argo cd", "tekton", "spinnaker"],
    "monitoring": ["prometheus", "grafana", "datadog", "new relic", "sentry", "loki", "elastic stack"],
    "serverless": ["aws lambda", "google cloud functions", "azure functions", "serverless framework"],
    "storage": ["s3", "ec2", "rds", "cloud run", "cloudflare", "firebase", "azure blob storage"],
    "testing": ["localstack", "terratest", "chaos monkey", "k6", "artillery"]
}

FRONT_ALL_STACK_LIST = ["react", "next.js", "vue", "nuxt.js", "angular", "svelte", "solid.js", "astro", "qwik",
                        "typescript", "javascript",
                        "tailwindcss", "bootstrap", "material-ui", "chakra-ui", "styled-components", "emotion", "sass", "less",
                        "redux", "zustand", "mobx", "recoil", "jotai", "tanstack-query", "swr",
                        "webpack", "vite", "rollup", "parcel", "turbopack",
                        "babel", "eslint", "prettier", "husky", "lint-staged",
                        "jest", "cypress", "playwright", "storybook", "vitest", "react-testing-library",
                        "graphql", "apollo client", "urql", "axios", "fetch",
                        "pwa", "webassembly", "three.js", "d3.js", "chart.js", "framer-motion",
                        "react-hook-form", "formik", "yup", "zod",
                        "i18next", "react-intl"]

BACK_ALL_STACK_LIST = ["node.js", "express", "nest.js", "koa", "fastify",
                       "spring", "spring boot", "java", "kotlin", "quarkus", "micronaut",
                       "django", "flask", "fastapi", "python", "tornado",
                       "ruby on rails", "laravel", "php", "asp.net", "c#", "go", "gin", "echo",
                       "graphql", "apollo server", "rest api", "swagger", "openapi",
                       "mysql", "postgresql", "mariadb",
                       "mongodb", "redis", "cassandra", "dynamodb", "couchbase",
                       "elasticsearch", "kafka", "rabbitmq", "nats", "grpc", "protobuf",
                       "docker", "kubernetes", "nginx", "apache",
                       "prisma", "typeorm", "sequelize", "sqlalchemy", "mongoose", "hibernate",
                       "jest", "mocha", "junit", "pytest", "mockito", "supertest"]

IOS_ALL_STACK_LIST = ["swift", "objective-c",
                      "swiftui", "uikit",
                      "coredata", "realm",
                      "alamofire", "moya",
                      "xctest", "quick", "nimble", "metrickit"]


CROSS_ALL_STACK_LIST = ["react native", "flutter", "xamarin",
                        "detox", "appium", "fastlane", "firebase test lab"]


ANDROID_ALL_STACK_LIST = ["kotlin", "java",
                          "android sdk", "android jetpack", "jetpack compose",
                          "room", "realm",
                          "retrofit", "okhttp",
                          "espresso", "junit", "mockk", "robolectric"]

GAME_ALL_STACK_LIST = ["unity", "unreal engine", "godot", "cryengine", "cocos2d-x", "gamemaker studio",
                       "blender", "maya", "3ds max", "openGL", "directX", "vulkan",
                       "fmod", "wwise",
                       "hlsl", "glsl",
                       "steamworks", "xbox live sdk", "psn sdk",
                       "unity test framework", "unreal automation", "gamelift"]

SECURITY_ALL_STACK_LIST = ["kali linux", "wireshark", "nmap", "metasploit", "burp suite", "nessus", "openvas", "snort", "suricata",
                           "osquery", "splunk", "elk stack", "nagios", "zabbix", "prometheus",
                           "hashcat", "john the ripper", "sqlmap", "aircrack-ng", "metasploit framework",
                           "cloudflare", "okta", "auth0", "mfa", "sso", "saml", "oauth2", "keycloak",
                           "veracrypt", "keepass", "gpg", "tor", "vpn", "vault",
                           "aqua", "twistlock", "snyk",
                           "owasp zap", "acunetix", "netsparker", "fortify", "checkmarx"]

CLOUD_ALL_STACK_LIST = ["aws", "gcp", "azure", "digitalocean", "oracle cloud", "naver cloud", "kakao cloud",
                        "docker", "kubernetes", "helm", "istio", "nginx", "rancher",
                        "terraform", "cloudformation", "pulumi", "ansible", "chef", "puppet", "cdk",
                        "jenkins", "github actions", "gitlab ci", "circleci", "argo cd", "tekton", "spinnaker",
                        "prometheus", "grafana", "datadog", "new relic", "sentry", "loki", "elastic stack",
                        "aws lambda", "google cloud functions", "azure functions", "serverless framework",
                        "s3", "ec2", "rds", "cloud run", "cloudflare", "firebase", "azure blob storage",
                        "localstack", "terratest", "chaos monkey", "k6", "artillery"]

entire_list = [FRONT_STACK_LIST, BACK_STACK_LIST, IOS_STACK_LIST, CROSS_STACK_LIST,
               ANDROID_STACK_LIST, GAME_STACK_LIST, SECURITY_STACK_LIST, CLOUD_STACK_LIST]

all_stack_list = [FRONT_ALL_STACK_LIST, BACK_ALL_STACK_LIST, IOS_ALL_STACK_LIST, CROSS_ALL_STACK_LIST,
                ANDROID_ALL_STACK_LIST, GAME_ALL_STACK_LIST, SECURITY_ALL_STACK_LIST, CLOUD_ALL_STACK_LIST]

sheet_names = ['FRONT_STACK_LIST', 'BACK_STACK_LIST', 'IOS_STACK_LIST', 'CROSS_STACK_LIST', 'ANDROID_STACK_LIST', 
               'GAME_STACK_LIST', 'SECURITY_STACK_LIST', 'CLOUD_STACK_LIST']