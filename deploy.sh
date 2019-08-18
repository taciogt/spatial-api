#!/usr/bin/env bash

set -x

#docker build . --tag taciogt/spatial-api
#docker push taciogt/spatial-api

CLUSTER=spatial-app
ECS_PROFILE=spatial-app-profile

#ecs-cli configure --cluster $CLUSTER --region us-east-1 --default-launch-type EC2 --config-name $CLUSTER
#
#ecs-cli configure profile --access-key $AWS_ACCESS_KEY_ID --secret-key $AWS_SECRET_ACCESS_KEY --profile-name $ECS_PROFILE
#
#ecs-cli up --force --keypair spatial-app --capability-iam --size 2 --instance-type t2.medium --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE

#ecs-cli compose up --create-log-groups --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE
#ecs-cli compose up --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE
#
#ecs-cli ps --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE
#ecs-cli compose down --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE
ecs-cli ps --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE

#ecs-cli compose scale 2 --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE

#ecs-cli compose service up --cluster-config $CLUSTER --ecs-profile $ECS_PROFILE