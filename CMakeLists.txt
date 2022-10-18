cmake_minimum_required(VERSION 3.16)

project(HowDoIUseAppveyor
	VERSION			0.0.0.0
	DESCRIPTION 	"Dummy project to learn to use appveyor"
	LANGUAGES		C CXX
)

set(HOWDOIUSEAPPVEYOR_SOURCES
	src/main.cpp
)

add_executable(${PROJECT_NAME}
	${HOWDOIUSEAPPVEYOR_SOURCES}
)