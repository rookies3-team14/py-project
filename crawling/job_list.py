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


ENTIRE_STACK_LIST = []


def get_entire_stack_list(stack_list: dict) -> None:
    for list in stack_list.values():
        ENTIRE_STACK_LIST.extend(list)


get_entire_stack_list(FRONT_STACK_LIST)
get_entire_stack_list(BACK_STACK_LIST)
get_entire_stack_list(IOS_STACK_LIST)
get_entire_stack_list(ANDROID_STACK_LIST)
get_entire_stack_list(CROSS_STACK_LIST)
get_entire_stack_list(GAME_STACK_LIST)
get_entire_stack_list(SECURITY_STACK_LIST)
get_entire_stack_list(CLOUD_STACK_LIST)

print(len(ENTIRE_STACK_LIST))
print(ENTIRE_STACK_LIST)
