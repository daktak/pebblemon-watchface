AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'chalk'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'chalk'
BUNDLE_NAME = 'pebblemon-watchface.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_CHALK', 'PBL_COLOR', 'PBL_ROUND', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=180', 'PBL_DISPLAY_HEIGHT=180', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['chalk']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'license': u'MIT', u'name': u'pebble-clay', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'author': u'Pebble Technology', u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, u'version': u'1.0.4', 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean', u'lint': u'./node_modules/.bin/eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)'}, u'keywords': [u'pebble', u'config', u'configuration', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'pebble': {u'sdkVersion': u'3', u'capabilities': [u'configurable'], u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, 'path': 'node_modules/pebble-clay/dist', u'homepage': u'https://github.com/pebble/clay#readme', u'description': u'Pebble Config Framework'}]
LIB_RESOURCES_JSON = {u'pebble-clay': []}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'ShakeSpriteChange': 10006, u'TimeStyle': 10004, u'MinuteColor': 10003, u'BackgroundBottomColor': 10001, u'BackgroundTopColor': 10000, u'HourTickmarks': 10005, u'HourColor': 10002, u'BatteryBar': 10007}
MESSAGE_KEYS_DEFINITION = '/mnt/c/Users/harri/Documents/pebble/pebblemon-watchface/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/mnt/c/Users/harri/Documents/pebble/pebblemon-watchface/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/mnt/c/Users/harri/Documents/pebble/pebblemon-watchface/build/js/message_keys.json'
NODE_PATH = '/home/linksky/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/linksky/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/linksky/.pebble-sdk/SDKs/current/sdk-core/pebble/chalk'
PEBBLE_SDK_ROOT = '/home/linksky/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['chalk', 'color', 'round', 'mic', 'strap', 'strappower', 'compass', 'health', '180w', '180h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'chalk', 'BUNDLE_BIN_DIR': 'chalk', 'BUILD_DIR': 'chalk', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_CHALK', 'PBL_COLOR', 'PBL_ROUND', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=180', 'PBL_DISPLAY_HEIGHT=180']}
PLATFORM_NAME = 'chalk'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'ShakeSpriteChange': 10006, u'TimeStyle': 10004, u'MinuteColor': 10003, u'BackgroundBottomColor': 10001, u'BackgroundTopColor': 10000, u'HourTickmarks': 10005, u'HourColor': 10002, u'BatteryBar': 10007}, u'watchapp': {u'watchface': True}, u'displayName': u'Pebblemon Time', u'uuid': u'2b5ff5d9-75a2-4f8e-866d-015216a3e45c', u'messageKeys': {u'ShakeSpriteChange': 10006, u'TimeStyle': 10004, u'MinuteColor': 10003, u'BackgroundBottomColor': 10001, u'BackgroundTopColor': 10000, u'HourTickmarks': 10005, u'HourColor': 10002, u'BatteryBar': 10007}, 'companyName': u'Harrison Allen', u'enableMultiJS': True, u'sdkVersion': u'3', 'versionLabel': u'1.0', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], 'longName': u'Pebblemon Time', 'shortName': u'Pebblemon Time', u'resources': {u'media': [{u'menuIcon': True, u'type': u'png', u'name': u'IMAGE_MENU_ICON', u'file': u'menu_icon.png'}, {u'type': u'raw', u'name': u'DATA_ANIMATION_TILESHEET', u'file': u'data/AnimationTilesheet.bin'}, {u'type': u'raw', u'name': u'DATA_WORLD_TILESHEET', u'file': u'data/WorldTilesheet.bin'}, {u'type': u'raw', u'name': u'DATA_CAVE', u'file': u'data/Cave.bin'}, {u'type': u'raw', u'name': u'DATA_FOREST', u'file': u'data/Forest.bin'}, {u'type': u'raw', u'name': u'DATA_NATIONAL_PARK', u'file': u'data/NationalPark.bin'}, {u'type': u'raw', u'name': u'DATA_ROUTE_1', u'file': u'data/Route1.bin'}, {u'type': u'raw', u'name': u'DATA_ROUTE_2', u'file': u'data/Route2.bin'}, {u'type': u'raw', u'name': u'DATA_SPRITESHEET', u'file': u'data/Spritesheet.bin'}, {u'type': u'raw', u'name': u'DATA_LOCATIONS', u'file': u'data/Locations.bin'}]}, 'name': u'pebblemon-watchface'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = [{u'menuIcon': True, u'type': u'png', u'name': u'IMAGE_MENU_ICON', u'file': u'menu_icon.png'}, {u'type': u'raw', u'name': u'DATA_ANIMATION_TILESHEET', u'file': u'data/AnimationTilesheet.bin'}, {u'type': u'raw', u'name': u'DATA_WORLD_TILESHEET', u'file': u'data/WorldTilesheet.bin'}, {u'type': u'raw', u'name': u'DATA_CAVE', u'file': u'data/Cave.bin'}, {u'type': u'raw', u'name': u'DATA_FOREST', u'file': u'data/Forest.bin'}, {u'type': u'raw', u'name': u'DATA_NATIONAL_PARK', u'file': u'data/NationalPark.bin'}, {u'type': u'raw', u'name': u'DATA_ROUTE_1', u'file': u'data/Route1.bin'}, {u'type': u'raw', u'name': u'DATA_ROUTE_2', u'file': u'data/Route2.bin'}, {u'type': u'raw', u'name': u'DATA_SPRITESHEET', u'file': u'data/Spritesheet.bin'}, {u'type': u'raw', u'name': u'DATA_LOCATIONS', u'file': u'data/Locations.bin'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1627280222
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/linksky/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
