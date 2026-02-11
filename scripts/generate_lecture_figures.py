#!/usr/bin/env python3
"""
Generate visualization figures for RSE course lectures.

This script creates all the matplotlib-based diagrams used in the lectures
and saves them as PNG files in their respective lecture directories.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                Rectangle, Polygon)
import os


def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)


def generate_lecture01_figures(output_dir):
    """Generate figures for Lecture 1: Git fundamentals."""
    print("Generating Lecture 1 figures...")
    
    # Figure 1: Git Three-Stage Workflow
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    
    boxes = [
        {'x': 0.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Working\nDirectory',
         'color': '#ffebee', 'desc': 'Edit files'},
        {'x': 3.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Staging\nArea',
         'color': '#fff3e0', 'desc': 'git add'},
        {'x': 6.5, 'y': 2, 'width': 2.5, 'height': 1.5, 'label': 'Repository\n(.git)',
         'color': '#e8f5e9', 'desc': 'git commit'}
    ]
    
    for box in boxes:
        fancy_box = FancyBboxPatch(
            (box['x'], box['y']), box['width'], box['height'],
            boxstyle="round,pad=0.1",
            edgecolor='#333', linewidth=2,
            facecolor=box['color']
        )
        ax.add_patch(fancy_box)
        ax.text(box['x'] + box['width']/2, box['y'] + box['height']/2 + 0.3,
                box['label'], ha='center', va='center',
                fontsize=12, fontweight='bold')
        ax.text(box['x'] + box['width']/2, box['y'] + box['height']/2 - 0.3,
                box['desc'], ha='center', va='center',
                fontsize=10, style='italic', color='#555')
    
    arrow1 = FancyArrowPatch((3, 2.75), (3.5, 2.75),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#1976d2')
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrowPatch((6, 2.75), (6.5, 2.75),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#1976d2')
    ax.add_patch(arrow2)
    
    ax.text(5, 4.5, 'Git Three-Stage Workflow', ha='center',
            fontsize=16, fontweight='bold')
    ax.text(5, 0.8, '1. Modify files → 2. Stage changes (git add) → 3. Commit to history (git commit)',
            ha='center', fontsize=11, color='#333',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f5f5f5', edgecolor='#999'))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'git_three_stage_workflow.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # Figure 2: Git Commit History Timeline
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-1, 2)
    ax.axis('off')
    
    commits = [
        {'x': 0, 'hash': 'a1b2c3d', 'msg': 'Initial commit', 'file': 'README.md'},
        {'x': 1, 'hash': 'e4f5g6h', 'msg': 'Add data processing', 'file': 'process.py'},
        {'x': 2, 'hash': 'i7j8k9l', 'msg': 'Fix bug in analysis', 'file': 'analysis.py'},
        {'x': 3, 'hash': 'm0n1o2p', 'msg': 'Add visualization', 'file': 'plot.py'},
        {'x': 4, 'hash': 'q3r4s5t', 'msg': 'Update documentation', 'file': 'README.md'},
    ]
    
    ax.plot([-0.3, 4.3], [0, 0], 'k-', linewidth=2, alpha=0.3)
    
    for commit in commits:
        circle = plt.Circle((commit['x'], 0), 0.15, color='#1976d2', zorder=3)
        ax.add_patch(circle)
        ax.text(commit['x'], -0.5, commit['hash'],
                ha='center', fontsize=9, family='monospace', color='#666')
        ax.text(commit['x'], 0.6, commit['msg'],
                ha='center', fontsize=9, fontweight='bold', color='#333')
        ax.text(commit['x'], 1.1, f"({commit['file']})",
                ha='center', fontsize=8, style='italic', color='#777')
    
    for i in range(len(commits) - 1):
        ax.annotate('', xy=(commits[i+1]['x'], 0), xytext=(commits[i]['x'], 0),
                    arrowprops=dict(arrowstyle='->', lw=2, color='#999'))
    
    ax.text(-0.3, -0.85, 'Oldest', ha='center', fontsize=10, color='#666')
    ax.text(4.3, -0.85, 'Newest', ha='center', fontsize=10, color='#666')
    ax.text(2, 1.7, 'Git Commit History Timeline', ha='center',
            fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'git_commit_timeline.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    # Figure 3: Local vs Remote Repository
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    local_box = FancyBboxPatch((0.5, 2), 3.5, 2.5,
                               boxstyle="round,pad=0.15",
                               edgecolor='#1976d2', linewidth=3,
                               facecolor='#e3f2fd')
    ax.add_patch(local_box)
    ax.text(2.25, 4, 'Your Computer', ha='center', fontsize=13, fontweight='bold')
    ax.text(2.25, 3.4, 'Local Repository', ha='center', fontsize=11)
    ax.text(2.25, 2.8, '(.git folder)', ha='center', fontsize=9, style='italic', color='#666')
    
    remote_box = FancyBboxPatch((6, 2), 3.5, 2.5,
                                boxstyle="round,pad=0.15",
                                edgecolor='#388e3c', linewidth=3,
                                facecolor='#e8f5e9')
    ax.add_patch(remote_box)
    ax.text(7.75, 4, 'GitHub', ha='center', fontsize=13, fontweight='bold')
    ax.text(7.75, 3.4, 'Remote Repository', ha='center', fontsize=11)
    ax.text(7.75, 2.8, '(Cloud backup)', ha='center', fontsize=9, style='italic', color='#666')
    
    push_arrow = FancyArrowPatch((4, 3.8), (6, 3.8),
                                 arrowstyle='->', mutation_scale=25,
                                 linewidth=2.5, color='#1976d2')
    ax.add_patch(push_arrow)
    ax.text(5, 4.2, 'git push', ha='center', fontsize=11,
            fontweight='bold', color='#1976d2')
    
    pull_arrow = FancyArrowPatch((6, 2.7), (4, 2.7),
                                 arrowstyle='->', mutation_scale=25,
                                 linewidth=2.5, color='#388e3c')
    ax.add_patch(pull_arrow)
    ax.text(5, 2.3, 'git pull', ha='center', fontsize=11,
            fontweight='bold', color='#388e3c')
    
    clone_arrow = FancyArrowPatch((7.75, 2), (2.25, 1.5),
                                  arrowstyle='->', mutation_scale=25,
                                  linewidth=2, color='#f57c00',
                                  linestyle='dashed')
    ax.add_patch(clone_arrow)
    ax.text(5, 1, 'git clone (first time)', ha='center', fontsize=10,
            style='italic', color='#f57c00')
    
    ax.text(5, 5.3, 'Git + GitHub Workflow', ha='center',
            fontsize=15, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'git_local_remote_workflow.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated 3 figures in {output_dir}")


def generate_lecture02_figures(output_dir):
    """Generate figures for Lecture 2: Git branching and merging."""
    print("Generating Lecture 2 figures...")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Fast-Forward Merge
    ax1.set_xlim(0, 12)
    ax1.set_ylim(0, 5)
    ax1.axis('off')
    ax1.set_title('Fast-Forward Merge', fontsize=14, fontweight='bold', pad=10)
    
    commits_ff = [
        {'x': 1, 'y': 2, 'label': 'A', 'branch': 'main', 'color': '#1976d2'},
        {'x': 2.5, 'y': 2, 'label': 'B', 'branch': 'main', 'color': '#1976d2'},
        {'x': 4, 'y': 3, 'label': 'C', 'branch': 'feature', 'color': '#f57c00'},
        {'x': 5.5, 'y': 3, 'label': 'D', 'branch': 'feature', 'color': '#f57c00'},
        {'x': 7, 'y': 3, 'label': 'E', 'branch': 'feature', 'color': '#f57c00'},
    ]
    
    for commit in commits_ff:
        circle = Circle((commit['x'], commit['y']), 0.3, color=commit['color'], zorder=3)
        ax1.add_patch(circle)
        ax1.text(commit['x'], commit['y'], commit['label'], ha='center', va='center',
                 fontsize=11, fontweight='bold', color='white')
    
    ax1.plot([1, 2.5], [2, 2], 'k-', linewidth=2, alpha=0.5)
    ax1.plot([2.5, 4], [2, 3], 'k-', linewidth=2, alpha=0.5)
    ax1.plot([4, 5.5, 7], [3, 3, 3], 'k-', linewidth=2, alpha=0.5)
    
    ax1.text(1, 1.3, 'main', ha='center', fontsize=10, fontweight='bold',
             color='#1976d2', bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                        edgecolor='#1976d2'))
    ax1.text(5.5, 3.7, 'feature', ha='center', fontsize=10, fontweight='bold',
             color='#f57c00', bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                        edgecolor='#f57c00'))
    
    ax1.annotate('', xy=(9, 2.5), xytext=(7.5, 3),
                 arrowprops=dict(arrowstyle='->', lw=2.5, color='#388e3c'))
    ax1.text(9.5, 2.5, 'main (after merge)', ha='left', va='center',
             fontsize=10, fontweight='bold', color='#388e3c')
    
    ax1.text(6, 0.5, 'No new merge commit needed - main just "fast-forwards" to include feature commits',
             ha='center', fontsize=10, style='italic', color='#555',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#e8f5e9',
                       edgecolor='#388e3c', linewidth=2))
    
    # Three-Way Merge
    ax2.set_xlim(0, 12)
    ax2.set_ylim(0, 5)
    ax2.axis('off')
    ax2.set_title('Three-Way Merge', fontsize=14, fontweight='bold', pad=10)
    
    commits_3way = [
        {'x': 1, 'y': 2.5, 'label': 'A', 'branch': 'both', 'color': '#1976d2'},
        {'x': 2.5, 'y': 2.5, 'label': 'B', 'branch': 'both', 'color': '#1976d2'},
        {'x': 4, 'y': 3.5, 'label': 'C', 'branch': 'feature', 'color': '#f57c00'},
        {'x': 5.5, 'y': 3.5, 'label': 'D', 'branch': 'feature', 'color': '#f57c00'},
        {'x': 4, 'y': 1.5, 'label': 'F', 'branch': 'main', 'color': '#1976d2'},
        {'x': 5.5, 'y': 1.5, 'label': 'G', 'branch': 'main', 'color': '#1976d2'},
    ]
    
    for commit in commits_3way:
        circle = Circle((commit['x'], commit['y']), 0.3, color=commit['color'], zorder=3)
        ax2.add_patch(circle)
        ax2.text(commit['x'], commit['y'], commit['label'], ha='center', va='center',
                 fontsize=11, fontweight='bold', color='white')
    
    ax2.plot([1, 2.5], [2.5, 2.5], 'k-', linewidth=2, alpha=0.5)
    ax2.plot([2.5, 4], [2.5, 3.5], 'k-', linewidth=2, alpha=0.5)
    ax2.plot([4, 5.5], [3.5, 3.5], 'k-', linewidth=2, alpha=0.5)
    ax2.plot([2.5, 4], [2.5, 1.5], 'k-', linewidth=2, alpha=0.5)
    ax2.plot([4, 5.5], [1.5, 1.5], 'k-', linewidth=2, alpha=0.5)
    
    ax2.text(5.5, 1, 'main', ha='center', fontsize=10, fontweight='bold',
             color='#1976d2', bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                        edgecolor='#1976d2'))
    ax2.text(5.5, 4, 'feature', ha='center', fontsize=10, fontweight='bold',
             color='#f57c00', bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                        edgecolor='#f57c00'))
    
    merge_circle = Circle((7.5, 2.5), 0.35, color='#388e3c', zorder=3)
    ax2.add_patch(merge_circle)
    ax2.text(7.5, 2.5, 'M', ha='center', va='center',
             fontsize=11, fontweight='bold', color='white')
    
    ax2.plot([5.5, 7.5], [3.5, 2.5], 'k-', linewidth=2, alpha=0.5)
    ax2.plot([5.5, 7.5], [1.5, 2.5], 'k-', linewidth=2, alpha=0.5)
    
    ax2.text(8.3, 2.5, 'Merge commit\n(combines both)', ha='left', va='center',
             fontsize=9, color='#388e3c', fontweight='bold')
    
    ax2.text(6, 0.5, 'Creates a merge commit to combine changes from both branches',
             ha='center', fontsize=10, style='italic', color='#555',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3e0',
                       edgecolor='#f57c00', linewidth=2))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'git_merge_strategies.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated 1 figure in {output_dir}")


def main():
    """Generate all lecture figures."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Generate figures for each lecture
    generate_lecture01_figures(os.path.join(base_dir, 'lecture_01'))
    generate_lecture02_figures(os.path.join(base_dir, 'lecture_02'))
    
    # TODO: Add remaining lectures (6, 8, 9, 10, 11, 12) in next commits
    
    print("\n✅ All figures generated successfully!")
    print("\nGenerated files:")
    print("  lecture_01/git_three_stage_workflow.png")
    print("  lecture_01/git_commit_timeline.png")
    print("  lecture_01/git_local_remote_workflow.png")
    print("  lecture_02/git_merge_strategies.png")


if __name__ == '__main__':
    main()


def generate_lecture06_figures(output_dir):
    """Generate figures for Lecture 6: CI/CD."""
    print("Generating Lecture 6 figures...")
    
    # CI Pipeline Workflow
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(7, 7.5, 'Continuous Integration Pipeline', ha='center',
            fontsize=16, fontweight='bold')
    
    dev_box = FancyBboxPatch((0.5, 4.5), 2, 2,
                             boxstyle="round,pad=0.1",
                             edgecolor='#1976d2', linewidth=2,
                             facecolor='#e3f2fd')
    ax.add_patch(dev_box)
    ax.text(1.5, 5.8, '👨‍💻 Developer', ha='center', fontsize=11, fontweight='bold')
    ax.text(1.5, 5.3, 'Pushes Code', ha='center', fontsize=10)
    ax.text(1.5, 4.9, 'to GitHub', ha='center', fontsize=9, style='italic')
    
    trigger_circle = Circle((4.5, 5.5), 0.4, color='#ff9800', zorder=3)
    ax.add_patch(trigger_circle)
    ax.text(4.5, 5.5, '⚡', ha='center', va='center', fontsize=20)
    ax.text(4.5, 4.3, 'Trigger', ha='center', fontsize=9, fontweight='bold')
    ax.text(4.5, 3.9, 'Automatic', ha='center', fontsize=8, style='italic')
    
    ci_box = FancyBboxPatch((6, 4), 3, 3,
                            boxstyle="round,pad=0.1",
                            edgecolor='#388e3c', linewidth=3,
                            facecolor='#e8f5e9')
    ax.add_patch(ci_box)
    ax.text(7.5, 6.5, '🤖 CI System', ha='center', fontsize=11, fontweight='bold')
    ax.text(7.5, 6, 'Clean Environment', ha='center', fontsize=9, color='#555')
    
    substeps = [
        {'y': 5.4, 'text': '1. Checkout code', 'icon': '📥'},
        {'y': 4.9, 'text': '2. Install dependencies', 'icon': '📦'},
        {'y': 4.4, 'text': '3. Run all tests', 'icon': '🧪'},
    ]
    for step in substeps:
        ax.text(6.3, step['y'], step['icon'], ha='left', fontsize=10)
        ax.text(6.7, step['y'], step['text'], ha='left', va='center', fontsize=8)
    
    pass_box = FancyBboxPatch((10.5, 5.5), 2.2, 1.2,
                              boxstyle="round,pad=0.08",
                              edgecolor='#2e7d32', linewidth=2,
                              facecolor='#c8e6c9')
    ax.add_patch(pass_box)
    ax.text(11.6, 6.3, '✅ PASS', ha='center', fontsize=11,
            fontweight='bold', color='#1b5e20')
    ax.text(11.6, 5.9, 'Tests succeeded', ha='center', fontsize=8)
    
    fail_box = FancyBboxPatch((10.5, 3.5), 2.2, 1.2,
                              boxstyle="round,pad=0.08",
                              edgecolor='#c62828', linewidth=2,
                              facecolor='#ffcdd2')
    ax.add_patch(fail_box)
    ax.text(11.6, 4.3, '❌ FAIL', ha='center', fontsize=11,
            fontweight='bold', color='#b71c1c')
    ax.text(11.6, 3.9, 'Tests failed', ha='center', fontsize=8)
    
    arrow1 = FancyArrowPatch((2.5, 5.5), (4.0, 5.5),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#333')
    ax.add_patch(arrow1)
    ax.text(3.25, 5.8, 'git push', ha='center', fontsize=8,
            style='italic', color='#666')
    
    arrow2 = FancyArrowPatch((5.0, 5.5), (6.0, 5.5),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#333')
    ax.add_patch(arrow2)
    
    arrow3 = FancyArrowPatch((9.0, 6.0), (10.5, 6.1),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#2e7d32')
    ax.add_patch(arrow3)
    
    arrow4 = FancyArrowPatch((9.0, 5.0), (10.5, 4.1),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#c62828')
    ax.add_patch(arrow4)
    
    feedback_arrow = FancyArrowPatch((10.5, 3.5), (2.5, 4.5),
                                     arrowstyle='->', mutation_scale=15,
                                     linewidth=1.5, color='#c62828',
                                     linestyle='dashed',
                                     connectionstyle="arc3,rad=-.3")
    ax.add_patch(feedback_arrow)
    ax.text(6, 2.5, 'Fix bugs & push again', ha='center', fontsize=9,
            style='italic', color='#c62828')
    
    ax.text(7, 1.5, '⏱️ Entire process: 2-5 minutes (fully automated)',
            ha='center', fontsize=10, color='#1976d2',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#e3f2fd',
                      edgecolor='#1976d2', linewidth=2))
    
    ax.text(7, 0.5, '✨ No manual testing • Consistent results • Immediate feedback',
            ha='center', fontsize=9, color='#555',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#f5f5f5',
                      edgecolor='#999'))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'ci_pipeline_workflow.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated 1 figure in {output_dir}")


def generate_lecture12_figures(output_dir):
    """Generate figures for Lecture 12: Workflow DAG."""
    print("Generating Lecture 12 figures...")
    
    # Workflow Dependency Graph (DAG)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(6, 9.5, 'Research Workflow Dependency Graph (DAG)', ha='center',
            fontsize=14, fontweight='bold')
    
    steps = [
        {'x': 6, 'y': 7.5, 'label': 'Download\nRaw Data', 'color': '#1976d2',
         'file': 'data/raw/temp.csv'},
        {'x': 6, 'y': 5.5, 'label': 'Clean &\nValidate', 'color': '#388e3c',
         'file': 'data/processed/\ntemp_clean.csv'},
        {'x': 3, 'y': 3.5, 'label': 'Generate\nPlots', 'color': '#f57c00',
         'file': 'results/\nplots.png'},
        {'x': 6, 'y': 3.5, 'label': 'Compute\nStatistics', 'color': '#f57c00',
         'file': 'results/\nstats.txt'},
        {'x': 9, 'y': 3.5, 'label': 'Run\nModel', 'color': '#f57c00',
         'file': 'results/\nmodel.pkl'},
        {'x': 6, 'y': 1.5, 'label': 'Generate\nReport', 'color': '#7b1fa2',
         'file': 'report.pdf'},
    ]
    
    for i, step in enumerate(steps):
        box = FancyBboxPatch((step['x'] - 1, step['y'] - 0.4), 2, 0.8,
                             boxstyle="round,pad=0.08",
                             edgecolor='black', linewidth=2,
                             facecolor=step['color'], alpha=0.8)
        ax.add_patch(box)
        
        ax.text(step['x'], step['y'], step['label'],
                ha='center', va='center', fontsize=9,
                color='white', fontweight='bold')
        
        ax.text(step['x'], step['y'] - 0.7, step['file'],
                ha='center', va='top', fontsize=7,
                style='italic', color='#666')
    
    dependencies = [
        (0, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5),
    ]
    
    for start_idx, end_idx in dependencies:
        start = steps[start_idx]
        end = steps[end_idx]
        arrow = FancyArrowPatch((start['x'], start['y'] - 0.5),
                                (end['x'], end['y'] + 0.5),
                                arrowstyle='->', mutation_scale=15,
                                linewidth=1.5, color='#333',
                                alpha=0.7)
        ax.add_patch(arrow)
    
    ax.annotate('', xy=(2.5, 3.5), xytext=(1.5, 3.5),
                arrowprops=dict(arrowstyle='<->', lw=1, color='#f57c00'))
    ax.annotate('', xy=(9.5, 3.5), xytext=(10.5, 3.5),
                arrowprops=dict(arrowstyle='<->', lw=1, color='#f57c00'))
    ax.text(6, 4.2, '← These 3 steps can run in parallel →',
            ha='center', fontsize=8, style='italic', color='#f57c00')
    
    ax.text(6, 0.3, '⚡ Smart execution: Only reruns steps when inputs change',
            ha='center', fontsize=9, color='#1976d2',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd',
                      edgecolor='#1976d2', linewidth=2))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'workflow_dag.png'),
                dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Generated 1 figure in {output_dir}")



def main():
    """Generate all lecture figures."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Generate figures for each lecture
    generate_lecture01_figures(os.path.join(base_dir, 'lecture_01'))
    generate_lecture02_figures(os.path.join(base_dir, 'lecture_02'))
    generate_lecture06_figures(os.path.join(base_dir, 'lecture_06'))
    generate_lecture12_figures(os.path.join(base_dir, 'lecture_12'))
    
    print("\n✅ All figures generated successfully!")
    print("\nGenerated files:")
    print("  lecture_01: git_three_stage_workflow.png, git_commit_timeline.png, git_local_remote_workflow.png")
    print("  lecture_02: git_merge_strategies.png")
    print("  lecture_06: ci_pipeline_workflow.png")
    print("  lecture_12: workflow_dag.png")


if __name__ == '__main__':
    main()
