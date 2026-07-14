from collections import Counter

from smart_repo.parser.models import RepositoryInfo


class RepositoryAnalytics:
    """
    Generate repository statistics.
    """

    def analyze(self, repository: RepositoryInfo):

        total_classes = 0
        total_functions = 0
        total_imports = 0
        total_calls = 0

        largest_file = None
        largest_size = 0

        imports_counter = Counter()

        for parsed_file in repository.files:

            total_classes += len(parsed_file.classes)
            total_functions += len(parsed_file.functions)
            total_imports += len(parsed_file.imports)
            total_calls += len(parsed_file.calls)

            if parsed_file.file.size > largest_size:

                largest_size = parsed_file.file.size
                largest_file = parsed_file.file.relative_path

            for imp in parsed_file.imports:
                imports_counter[imp.module] += 1

        return {
            "repository": repository.name,
            "python_files": len(repository.files),
            "classes": total_classes,
            "functions": total_functions,
            "imports": total_imports,
            "calls": total_calls,
            "largest_file": largest_file,
            "largest_size": largest_size,
            "top_imports": imports_counter.most_common(10),
        }