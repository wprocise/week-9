mkdir /temp_grader
cp -r /autograder/tests /temp_grader/tests
cp -r . /temp_grader
cd /temp_grader
python -m unittest -v tests/test_all.py > /workspaces/week-9/output.txt 2>&1
cd /workspaces/week-9
rm -r /temp_grader
# sed -i '1s/^/Output: \n```python\n/' output.txt
# echo "\`\`\`" >> output.txt