#!/bin/bash
set -e
echo "Deploying with token $DEPLOY_TOKEN"
git push origin main --force
