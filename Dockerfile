# Sandbox image for this problem's checker.
#
# Deliberately minimal: the whole point is that a solver can read this file in
# ten seconds and know exactly what will run. Add nothing that is not needed to
# execute check.py.
FROM python:3.12-slim
WORKDIR /task
COPY check.py /task/check.py
USER 65534:65534
ENTRYPOINT ["python3", "/task/check.py"]
